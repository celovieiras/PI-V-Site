import streamlit as st

#config. aplicação streamlit
st.set_page_config(page_title="Projeto Trepidação - PI-V", layout="wide")

imagem_logo = "images/fatec_logo.png"
st.logo(image=imagem_logo, icon_image=imagem_logo)
st.image(imagem_logo, output_format="PNG")
st.title("Análise de trepidação em ambiente doméstico")
st.text("Trabalho realizado por Marcelo Vieira da Silva e Thiago Ribeiro da Silva para Projeto Integrador V")
st.write("---")

with st.container():
    st.header("Sobre o projeto:")