import dotenv
import streamlit as st
import pandas as pd
import datetime as dt
from pymongo import MongoClient
import dotenv
import os

# carregando .env
dotenv.load_dotenv(dotenv.find_dotenv())
user_mongo_access = os.getenv("USER_MONGO_ACCESS")
client = MongoClient(user_mongo_access)
db = client["db_acelerometro"]

#config. aplicação streamlit
st.set_page_config(page_title="Projeto Trepidação - PI-V", layout="wide")

@st.cache_data
def load_dataframe():
    collection = db["acelerometro"]
    dados = list(collection.find({}))
    df = pd.DataFrame(dados)
    df.head()
    df["dt_trep"] = df['dt_cria'].dt.date
    df['hr_trep'] = df['dt_cria'].dt.time
    return df

data = load_dataframe()

#imagem_logo = "images/fatec_logo.png"
#st.image(imagem_logo)
st.title("Análise de trepidação em ambiente doméstico")
st.text("Trabalho realizado por Marcelo Vieira da Silva e Thiago Ribeiro da Silva para Projeto Integrador V")

with st.container():
    st.header("Sobre o projeto:")