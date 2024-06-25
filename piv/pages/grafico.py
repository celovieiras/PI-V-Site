import streamlit as st
import pandas as pd
import datetime as dt
from pymongo import MongoClient
import dotenv
import os
import plotly.express as px

st.set_page_config(page_title='Visualização da trepidação', layout='wide')
# carregando .env
dotenv.load_dotenv(dotenv.find_dotenv())
user_mongo_access = os.getenv("MONGO_ACCESS")
client = MongoClient(user_mongo_access)
db = client["db_acelerometro"]

@st.cache_data
def load_dataframe():
    collection = db["acelerometro"]
    dados = list(collection.find({}))
    df = pd.DataFrame(dados)
    df['dt_cria'] = pd.to_datetime(df["dt_cria"])
    df["dt_trep"] = df['dt_cria'].dt.date
    df['hr_trep'] = df['dt_cria'].dt.time
    return df

data = load_dataframe()
val_dt_padrao = dt.date(2024,5,30)

# imagem_logo = "images/fatec_logo.png"
# st.logo(imagem_logo, icon_image=imagem_logo)
# st.image(imagem_logo, output_format="PNG")
st.title("Análise de trepidação em ambiente doméstico")
exclui_zero_trep = data['acelerometroZ'][data['acelerometroZ'] != 0]
valor_min_trep = exclui_zero_trep.min()
valor_max_trep = data['acelerometroZ'].max()
valor_med_trep = data['acelerometroZ'].mean()


with st.container():
    st.header("Selecione as opções abaixo:")
    st.write("---")

    with st.container():

            col, col2 = st.columns(2)
            with col:
                dt_trep = st.date_input("Selecione a data da trepidação", value=val_dt_padrao, format="DD/MM/YYYY")
                st.write(f"Menor valor de trepidação registrado: {valor_min_trep}")
                st.write(f"Valor médio das trepidações: {round(valor_med_trep, 2)}")                

            with col2:
                hr_trep = st.time_input("Selecione a hora", value=dt.time(0, 0), step=3600)
                st.write(f"Maior valor de trepidação registrado: {valor_max_trep}")

    with st.container():
        dt_hora_selec = dt.datetime.combine(dt_trep, hr_trep)
        filtros_grafico = data[data['dt_cria'] >= dt_hora_selec]

        filtros_grafico['diff'] = filtros_grafico['acelerometroZ'].diff().fillna(0).abs()
        change_threshold = 0
        momentos_trepidacao = filtros_grafico[(filtros_grafico['diff'] > change_threshold) & (filtros_grafico['acelerometroZ'] != 0)]
        fig = px.line(momentos_trepidacao.set_index('dt_cria')['acelerometroZ'], title='Registros de trepidação')
        # st.line_chart(momentos_trepidacao.set_index('dt_cria')['acelerometroZ'], color='#FEA82F', use_container_width=True)
        st.plotly_chart(fig, use_container_width=True)
        
    with st.container():
        dt_hora_selec = dt.datetime.combine(dt_trep, hr_trep)
        filtros_grafico = data[data['dt_cria'].isin(dt_hora_selec)]

        filtros_grafico['diff'] = filtros_grafico['acelerometroZ'].diff().fillna(0).abs()
        change_threshold = 0
        momentos_trepidacao = filtros_grafico[(filtros_grafico['diff'] > change_threshold) & (filtros_grafico['acelerometroZ'] != 0)]
        fig = px.line(momentos_trepidacao.set_index('dt_cria')['acelerometroZ'], title='Registros de trepidação')
        # st.line_chart(momentos_trepidacao.set_index('dt_cria')['acelerometroZ'], color='#FEA82F', use_container_width=True)
        st.plotly_chart(fig, use_container_width=True)