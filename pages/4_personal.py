import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="Pessoal",
    page_icon="",
    layout="wide"
)

df4 = st.session_state["personal"]

st.sidebar.write("Subsecretariat")

fracoes = df4["Fracao"].value_counts().index
fracao = st.sidebar.selectbox("Fração", fracoes)

Nomes = df4[df4["Fracao"] == fracao]["NOMBRE/APELLIDOS"]
Name = st.sidebar.selectbox("Name", Nomes)

dados = df4[df4["NOMBRE/APELLIDOS"] == Name]
foto = dados.iloc[0,-1]
try:
    st.image(foto)
except:
    st.write("Sem foto")

st.title(f"{dados.iloc[0, 3]}")
st.markdown(f"**Função:** {dados.iloc[0, 1]}")
grafico = df4["País Origen"].value_counts()

col1, col2, col3 = st.columns(3)
with col1:
    col1.markdown(f"**País:** {dados.iloc[0, 7]}")
    st.divider()
    st.bar_chart(grafico)

with col2:
    col2.markdown(f"**Situação:** {dados.iloc[0, 6]}")
    st.divider()

with col3:
    col3.markdown(f"**Fim da missão:** {dados.iloc[0, 5]}")
    st.divider()

st.divider()





