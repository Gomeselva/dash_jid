import streamlit as st
import pandas as pd
import webbrowser
from datetime import datetime
import os
import base64

st.set_page_config(
    page_title="home",
    page_icon="",
    layout="wide"
)

st.image("pictures\images.png", use_column_width=True)

btn = st.button("Carta da OEA")
if btn:
    webbrowser.open_new_tab("http://www.oas.org/dil/port/tratados_A-41_Carta_da_Organiza%C3%A7%C3%A3o_dos_Estados_Americanos.htm")


df1 = pd.read_excel("docs\Pasta1.xlsx")
df1
st.session_state["data"] = df1

# df_ = df1.loc[:, ["Account Number", "Category", "Income ACC", "Funding Source", "TOTAL INCOME  IADB/OAS", "YTD"]]
# df_balance = df_.groupby("Funding Source")["YTD"].sum()
# st.session_state["balance"] = df_balance

# df2 = pd.read_excel("/Users/fabiobarbosa/Desktop/JID_site_dados/dataset/general_whitdrawals.xlsx")
# df_2 = df2.loc[:, ["Organ", "Acc No", "Category", "Exp. Acc", "TOTAL OPS BUDGET CY23", "YTD", "BALANCE"]]
# df_dist = df2.groupby("Organ")["TOTAL OPS BUDGET CY23"].sum()
# df_currently = df2.groupby("Organ")["BALANCE"].sum()
# st.session_state["Organ"] = df_currently
# st.session_state["table"] = df_2


# df3 = df2.loc[:,["Organ", "Category", "Exp. Acc", "YTD", "BALANCE"]]
# df4 = pd.read_excel("/Users/fabiobarbosa/Desktop/JID_site_dados/dataset/Efetivo.xlsx", index_col=0)
# st.session_state["personal"] = df4


# df = pd.read_excel("/Users/fabiobarbosa/Desktop/JID_site_dados/dataset/plano_trabalho.xlsx")
# st.session_state["plan"] = df

# for i in ["balance", "Organ", "personal"]:
#     if i not in st.session_state:
#         df1 = pd.read_excel("/Users/fabiobarbosa/Desktop/JID_site_dados/dataset/general_balance.xlsx")
#         df_ = df1.loc[:, ["Account Number", "Category", "Income ACC", "Funding Source", "TOTAL INCOME  IADB/OAS", "YTD"]]
#         df_balance = df_.groupby("Funding Source")["YTD"].sum()
#         st.session_state["balance"] = df_balance

#         df2 = pd.read_excel("/Users/fabiobarbosa/Desktop/JID_site_dados/dataset/general_whitdrawals.xlsx")
#         df_2 = df2.loc[:, ["Organ", "Acc No", "Category", "Exp. Acc", "TOTAL OPS BUDGET CY23", "YTD", "BALANCE"]]
#         df_dist = df2.groupby("Organ")["TOTAL OPS BUDGET CY23"].sum()
#         df_currently = df2.groupby("Organ")["BALANCE"].sum()
#         st.session_state["Organ"] = df_currently
#         st.session_state["table"] = df_2

#         df3 = df2.loc[:,["Organ", "Category", "Exp. Acc", "YTD", "BALANCE"]]
#         df4 = pd.read_excel("/Users/fabiobarbosa/Desktop/JID_site_dados/dataset/Efetivo.xlsx", index_col=0)
#         st.session_state["personal"] = df4


# st.sidebar.markdown("**Documents:**")
# st.sidebar.markdown("[documento](http://www.oas.org/dil/port/tratados_A-41_Carta_da_Organiza%C3%A7%C3%A3o_dos_Estados_Americanos.htm)")

# list_1 = os.listdir("/Users/fabiobarbosa/Desktop/JID_site_dados/Docs_JID")

# # for i in os
# path = "/Users/fabiobarbosa/Desktop/JID_site_dados/Docs_JID/"

# col1, col2, col3 = st.columns(3)
# with col1:
#     with st.container():
#         list_2 = []
#         st.markdown("**Documents:**")

#         for i in list_1:
#             btn = st.button(i[:-4])
#             list_2.append(btn)


# def show_pdf(file_path):
#     with open(file_path, "rb") as f:
#         base64_pdf = base64.b64encode(f.read()).decode("utf-8")
#     pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="800" height="800" type="application/pdf"></iframe>'
#     st.markdown(pdf_display, unsafe_allow_html=True)

# with col2:
#     with st.container():
#         for i in range(len(list_2)):
#             if list_2[i]:
#                 try:
#                         show_pdf(path + list_1[i])
#                 except: 
#                     print("select the document")

    
