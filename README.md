# Projeto 07 — Bike Sharing Demand (UCI)

Prever a demanda diária de bicicletas de um sistema de aluguel usando dados do **Bike Sharing Dataset (UCI)**.

## Objetivo
Criar um pipeline simples de **EDA → preparação → modelagem → avaliação → mini dashboard (Streamlit)** e publicar no GitHub.

## Dataset
- Origem: *UCI Machine Learning Repository – Bike Sharing Dataset*.
- Arquivos esperados na pasta `data/raw/`: `day.csv` (diário) e opcionalmente `hour.csv` (horário).
- Se você ainda não baixou, use o dataset oficial (coloque `day.csv` em `data/raw/`). Enquanto isso, existe um **dataset sintético** em `data/sample/day_sample.csv` para testes rápidos.

## Como rodar (passo a passo)
1. **Criar ambiente** (Windows PowerShell ou macOS/Linux):
   ```bash
   python -m venv .venv
   # Ativar
   # Windows:
   .venv\Scripts\Activate.ps1
   # macOS/Linux:
   source .venv/bin/activate

   pip install -r requirements.txt
   ```

2. **Colocar os dados**:
   - Se já tiver o original `day.csv`, coloque em `data/raw/day.csv`.
   - Se não tiver, o pipeline usa `data/sample/day_sample.csv` automaticamente.

3. **Preparar dados**:
   ```bash
   python src/prepare.py
   ```

4. **Treinar modelo**:
   ```bash
   python src/train.py
   ```

   Saídas:
   - Modelo salvo em `models/model.joblib`
   - Métricas em `reports/metrics.json`
   - Gráfico em `reports/figures/actual_vs_pred.png`

5. **Exploração em notebook** (opcional):
   ```bash
   jupyter lab
   ```
   Abra `notebooks/01-EDA.ipynb` e `notebooks/02-modeling.ipynb`.

6. **Dashboard (Streamlit)**:
   ```bash
   streamlit run app/app.py
   ```

## Estrutura do repositório
```
project-07-bike-sharing/
├─ data/
│  ├─ raw/                 # coloque day.csv aqui
│  ├─ processed/           # arquivos processados (gerados)
│  └─ sample/              # dataset sintético para testes
├─ notebooks/
│  ├─ 01-EDA.ipynb
│  └─ 02-modeling.ipynb
├─ src/
│  ├─ prepare.py
│  ├─ train.py
│  ├─ evaluation.py
│  └─ utils.py
├─ models/
├─ reports/
│  └─ figures/
├─ app/
│  └─ app.py
├─ requirements.txt
├─ .gitignore
└─ README.md
```

## Métricas principais
- **RMSE** e **R²** para avaliar a qualidade das previsões de `cnt` (demanda total).

## Próximos passos
- Tunar hiperparâmetros com `RandomizedSearchCV`.
- Adicionar validação temporal com `TimeSeriesSplit`.
- Incluir variáveis externas (feriados específicos, chuva, etc.) se disponíveis.

---

> Dica: sempre faça commits pequenos e claros. Ex.: `feat(eda): basic plots by month`.