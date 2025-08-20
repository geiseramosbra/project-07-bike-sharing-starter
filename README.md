# Projeto  — Bike Sharing Demand (UCI)

# Bike Sharing Analysis

Este projeto consiste em uma **análise exploratória de dados (EDA)** de um dataset de compartilhamento de bicicletas, utilizando **Python**, **SQL** e bibliotecas de visualização como **Matplotlib** e **Seaborn**.

O objetivo é demonstrar habilidades em:
- Manipulação e limpeza de dados com **Pandas**
- Consultas **SQL** aplicadas a DataFrames
- Criação de visualizações para insights de negócios
- Preparação de projeto para portfólio no GitHub

---

## 🔹 Dataset

O dataset utilizado é `day_sample.csv`, que contém registros diários de uso de bicicletas compartilhadas. Algumas das colunas importantes:

| Coluna       | Descrição |
|--------------|-----------|
| `dteday`     | Data do registro |
| `season`     | Estação do ano (1=Primavera, 2=Verão, 3=Outono, 4=Inverno) |
| `yr`         | Ano (0=2011, 1=2012) |
| `mnth`       | Mês do ano |
| `cnt`        | Total de aluguéis |
| `casual`     | Usuários casuais |
| `registered` | Usuários registrados |
| `temp`       | Temperatura normalizada |
| `hum`        | Umidade normalizada |
| `windspeed`  | Velocidade do vento normalizada |

---

## 🔹 Ferramentas e Bibliotecas

- Python 3.x  
- Pandas  
- Matplotlib  
- Seaborn  
- SQLAlchemy (para consultas SQL em DataFrames)  

---

## 🔹 Passos Realizados

1. **Carregamento do CSV**
   ```python
   df = pd.read_csv('../data/sample/day_sample.csv')


## 🔹 Criação de colunas extras

season_name → nome da estação
year, month, day → extraídos da data

## 🔹 Criação de engine SQL em memória

from sqlalchemy import create_engine
engine = create_engine("sqlite://", echo=False)
df.to_sql("bike", con=engine, index=False, if_exists="replace")

## 🔹 Consultas SQL e visualizações

Média de aluguéis por estação
Top 10 dias com maior número de aluguéis
Comparação entre usuários casuais e registrados

## 🔹 Visualizações

Gráficos de barras utilizando Seaborn para ilustrar insights

## 🔹 Como Rodar

#Clone este repositório: 

git clone https://github.com/seu-usuario/bike-sharing-analysis.git
cd bike-sharing-analysis

#Instale as dependências:

pip install pandas matplotlib seaborn sqlalchemy

#Abra o notebook:

jupyter notebook Bike_Sharing_Analysis.ipynb




