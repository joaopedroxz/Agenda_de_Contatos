import streamlit as st
#import pandas as pd

st.set_page_config(page_title="Agenda de Contatos")

with st.container():
    st.title("Agenda de Contatos")
    st.write('---')
    opc = st.sidebar.selectbox("Outras opções:", ("Buscar contato",))
    st.subheader("Adicionar novo contato:")
    nome = st.text_input("Nome:")
    numero = st.text_input("Número:")
    categoria = st.selectbox("Categoria:", ["Familiares", "Amigos", "Conhecidos"])
    if st.button("Salvar"):
        st.write("Contato salvo")

with st.container():
    st.subheader("Remover contato:")
    nome_remove = st.text_input("Nome do contato a ser removido:")
    if st.button('Remover'):
        st.write("Contato removido")

