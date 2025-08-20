import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

st.set_page_config(page_title="Bike Sharing — Previsor", page_icon="🚲", layout="centered")

st.title("🚲 Bike Sharing — Previsor de Demanda (Diário)")

model_path = Path(__file__).resolve().parents[1] / 'models' / 'model.joblib'
if model_path.exists():
    model = joblib.load(model_path)
    st.success("Modelo carregado com sucesso!")
else:
    st.warning("Modelo não encontrado. Rode `python src/prepare.py` e `python src/train.py` antes.")
    model = None

st.subheader("Entrada de variáveis")
season = st.selectbox("season (1-primavera, 2-verão, 3-outono, 4-inverno)", [1,2,3,4], index=1)
yr = st.selectbox("yr (0=2011, 1=2012)", [0,1], index=1)
mnth = st.slider("mnth (1-12)", 1, 12, 6)
holiday = st.selectbox("holiday", [0,1])
weekday = st.slider("weekday (0=Seg .. 6=Dom)", 0, 6, 2)
workingday = st.selectbox("workingday", [0,1], index=1)
weathersit = st.selectbox("weathersit (1-bom, 2-neutro, 3-ruim)", [1,2,3], index=0)
temp = st.slider("temp (0-1 normalizado)", 0.0, 1.0, 0.6, 0.01)
atemp = st.slider("atemp (0-1 normalizado)", 0.0, 1.0, 0.58, 0.01)
hum = st.slider("hum (0-1)", 0.0, 1.0, 0.6, 0.01)
windspeed = st.slider("windspeed (0-1)", 0.0, 1.0, 0.2, 0.01)
dayofyear = st.slider("dayofyear (1-366)", 1, 366, 180)
weekofyear = st.slider("weekofyear (1-53)", 1, 53, 26)

cols = ['season','yr','mnth','holiday','weekday','workingday','weathersit',
        'temp','atemp','hum','windspeed','dayofyear','weekofyear']

row = [[season,yr,mnth,holiday,weekday,workingday,weathersit,
        temp,atemp,hum,windspeed,dayofyear,weekofyear]]
X = pd.DataFrame(row, columns=cols)

if st.button("Prever demanda (cnt)"):
    if model is None:
        st.error("Treine o modelo primeiro.")
    else:
        pred = float(model.predict(X)[0])
        st.metric("Demanda prevista (cnt)", f"{pred:,.0f}")