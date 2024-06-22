import streamlit as st

#config. aplicação streamlit
st.set_page_config(page_title="Projeto Trepidação - PI-V", layout="wide")

st.title("Análise de trepidação em ambiente doméstico")
st.text("Trabalho realizado por Marcelo Vieira da Silva e Thiago Ribeiro da Silva para Projeto Integrador V")
st.write("---")

with st.container():
    st.header("Sobre o projeto:")
    st.text("O projeto de captura de trepidação em ambiente doméstico consiste no desenvolvimento de  um dispositivo capaz de realizar a captura de vibração em um \nambiente doméstico, registrando os possíveis momentos de pico e como influencia na vida de moradores. Tem por objetivo: O registro de dados de vibração em \nambiente doméstico e possíveis momentos de pico, como por exemplo, em uma moradia que esteja próximo a terreno com obras ou próximo a avenidas ou região com movimento de tráfego intenso.")
    st.text("Através desse projeto, será possível analisar os possíveis momentos de pico de trepidação no ambiente doméstico ou região por meio dados de medidas de \nvibração e horário no qual ocorre e propor possíveis soluções por meio da análise e visualização de dados em conjunto com parcerias como orgãos reguladores e governo.")