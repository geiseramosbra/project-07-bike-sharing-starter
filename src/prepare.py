import pandas as pd
from pathlib import Path
from utils import path

raw_day = path('data', 'raw', 'day.csv')
sample_day = path('data', 'sample', 'day_sample.csv')
processed = path('data', 'processed', 'day_processed.csv')

def main():
    if raw_day.exists():
        df = pd.read_csv(raw_day)
        print('Usando dados oficiais:', raw_day)
    else:
        df = pd.read_csv(sample_day)
        print('ATENÇÃO: usando dataset sintético (coloque day.csv em data/raw para usar o oficial)')

    df['dteday'] = pd.to_datetime(df['dteday'])
    df = df.sort_values('dteday')

    # (Opcional) Feature engineering simples
    df['dayofyear'] = df['dteday'].dt.dayofyear
    df['weekofyear'] = df['dteday'].dt.isocalendar().week.astype(int)

    df.to_csv(processed, index=False)
    print('Salvo processado em:', processed)

if __name__ == '__main__':
    main()