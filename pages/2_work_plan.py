import streamlit as st
import pandas as pd

st.session_state["data"]

# df = st.session_state["plan"]
# df["Resp"].value_counts()
# st.sidebar.markdown("**Strategic Plan:**")

# objetivos = df["Objetivo Estratégico"].value_counts().index

# obj = st.sidebar.selectbox("Objetivos", objetivos)
# df_tareas = df[df["Objetivo Estratégico"]== obj]
# df_1 = df[df["Objetivo Estratégico"] == obj] 

# resp = df_1["Resp"].value_counts()

# col1, col2 = st.columns([0.3, 0.7])

# with col1:
#     st.write("Qtd Tarefas")
#     st.write(len(df_1["Tarefa"].unique()))
#     st.divider()
#     st.write("Qtd Ações")
#     st.write(len(df_1["Ação"].unique()))
#     st.bar_chart(resp)


# # tarefas = df_1["Tarefa"].value_counts()
