import json
from pathlib import Path

import joblib
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.ensemble import RandomForestRegressor

from utils import path
from evaluation import regression_metrics

processed = path('data', 'processed', 'day_processed.csv')
metrics_path = path('reports', 'metrics.json')
fig_path = path('reports', 'figures', 'actual_vs_pred.png')
model_path = path('models', 'model.joblib')

FEATURES = ['season','yr','mnth','holiday','weekday','workingday','weathersit',
            'temp','atemp','hum','windspeed','dayofyear','weekofyear']
TARGET = 'cnt'

def main():
    if not processed.exists():
        print('Arquivo processado não encontrado. Execute: python src/prepare.py')
        return

    df = pd.read_csv(processed)
    df = df.sort_values('dteday')

    X = df[FEATURES]
    y = df[TARGET]

    # Split temporal (80/20)
    split_idx = int(len(df)*0.8)
    X_train, X_test = X.iloc[:split_idx], X.iloc[split_idx:]
    y_train, y_test = y.iloc[:split_idx], y.iloc[split_idx:]

    model = RandomForestRegressor(n_estimators=400, random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    m = regression_metrics(y_test, y_pred)
    print('Métricas:', m)

    # Persistir
    model_path.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, model_path)
    with open(metrics_path, 'w', encoding='utf-8') as f:
        json.dump(m, f, indent=2)

    # Plot simples
    plt.figure()
    plt.plot(y_test.values, label='Real')
    plt.plot(y_pred, label='Previsto')
    plt.title('Real vs Previsto (teste)')
    plt.xlabel('Tempo (índice)')
    plt.ylabel('cnt')
    plt.legend()
    fig_path.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(fig_path, bbox_inches='tight', dpi=120)
    plt.close()

    print('Modelo salvo em:', model_path)
    print('Métricas salvas em:', metrics_path)
    print('Figura salva em:', fig_path)

if __name__ == '__main__':
    main()