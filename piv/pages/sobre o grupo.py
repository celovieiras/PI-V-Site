import streamlit as st

st.set_page_config(page_title='Grupo', layout='wide')
imagem_logo = "images/fatec_logo.png"
st.logo(imagem_logo, icon_image=imagem_logo)
st.image(imagem_logo, output_format="PNG")
st.title("Sobre o grupo")
