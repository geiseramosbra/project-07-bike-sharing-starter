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
