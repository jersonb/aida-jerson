
import streamlit as st
import pandas as pd


pd.set_option("float_format",'{:.2f}'.format)
df = pd.read_csv(filepath_or_buffer='./data/2022.csv', sep='|', low_memory=False)
df["data_empenho"] = pd.to_datetime(df["data_empenho"])
df["trimestre_empenho"] = df["data_empenho"].dt.quarter
valor_total = df["valor_empenhado"].sum()

valores_unidades_orcamentarias = df[["unidade_orcamentaria","valor_empenhado"]].groupby("unidade_orcamentaria").sum()
valores_unidades_orcamentarias["%"] = valores_unidades_orcamentarias["valor_empenhado"].div(valor_total)*100
valores_unidades_orcamentarias.sort_values("valor_empenhado", ascending=False)

percentual_trimestre = df[["trimestre_empenho","valor_empenhado"]].groupby(["trimestre_empenho"]).sum()
percentual_trimestre["valor_empenhado"] = percentual_trimestre["valor_empenhado"].div(valor_total)*100


st.html('<h1>Texto em html</h1>')
st.markdown('# Texto Markdown')


val_slider = st.slider("teste",10,30)

st.metric('Valor Total',val_slider, delta='olé' )
col1, col2, col3 = st.columns(3)

with col1:
    st.table(percentual_trimestre)

with col2:
    st.area_chart(percentual_trimestre)

with col3:
    st.bar_chart(percentual_trimestre)