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

'''
#parteroberth
class contato:
    def __init__(self, nome, numero, categoria):
        self.nome = nome
        self.numero = numero
        self.categoria = categoria
        self.proximo = None
        self.anterior = None

class Listacontatos:
    def __init__(self):
        self.cabeca = None
        self.cauda = None

    def inserção(self, nome, numero, categoria):
        novo_contato = contato(nome, numero, categoria)
        novo_contato.proximo = self.cabeca
        if self.cabeca:
            self.cabeca.anterior = novo_contato
        else:
            self.cauda = novo_contato
        self.cabeca = novo_contato


    def deletar_final(self):
        if not self.cabeca:
            return
        if not self.cabeca.proximo:
            self.cabeca = None
            self.cauda = None
            return
        self.cauda.anterior.proximo = None
        self.cauda = self.cauda.anterior

    def travessia(self):
        atual = self.cabeca
        while atual:
            print(atual.nome,atual.numero,atual.categoria)
            atual = atual.proximo


# operaçoes
lista = Listacontatos()

#inseçoes
print("quantas inserçoes?")
vezes_inserção = int(input())
for i in range(vezes_inserção):
    nome, numero , categoria = input().split(",")
    numero = int(numero)
    lista.inserção(nome, numero, categoria)

#deleção
print("quantas deleçoes?")
vezes_deleçoes = int(input())
for i in range(vezes_deleçoes):
    lista.deletar_final()

#travessia
print("Travessia após deleções:")
lista.travessia()
'''
