import streamlit as st
import pandas as pd

st.set_page_config(page_title="Agenda de Contatos")

with st.container():
    st.title("Agenda de Contatos")
    st.write('---')
with st.container():
    opc = st.sidebar.selectbox("Outras opções:", ("Buscar contato", "Enviar email",))
    if opc == "Buscar contato":
        st.subheader("Buscar")
        st.text_input("Digite o nome de um contato para buscar:")
with st.container():
    st.subheader("Adicionar novo contato:")
    nome = st.text_input("Nome:")
    numero = st.text_input("Número:", help="(00) 00000-0000")
    categoria = st.selectbox("Categoria:", ["Familiares", "Amigos", "Conhecidos"])
    if st.button("Salvar", help="Clique aqui para salvar"):
        st.write("Contato salvo")
with st.container():
    st.subheader("Remover contato:")
    nome_remove = st.text_input("Nome do contato a ser removido:")
    if st.button('Remover', help="Clique aqui para remover"):
        st.write("Contato removido")

#JUNÇÃO DOS CÓDIGOS
import streamlit as st

class contato:
    def __init__(self, nome, numero):
        self.nome = nome
        self.numero = numero
        self.proximo = None
        self.anterior = None

class Listacontatos:
    def __init__(self):
        self.cabeca = None
        self.cauda = None

    def adicionar_no_final(self, nome, numero):
        novo_no = contato(nome, numero)
        if self.cabeca is None:
            self.cabeca = novo_no
            self.cauda = novo_no
        else:
            novo_no.anterior = self.cauda
            self.cauda.proximo = novo_no
            self.cauda = novo_no

st.set_page_config(page_title="Agenda de Contatos")


@st.cache(allow_output_mutation=True)
def obter_ou_criar_lista():
    return Listacontatos()

lista_dupla = obter_ou_criar_lista()

st.header("Sua Agenda de Contatos:")
no_atual = lista_dupla.cabeca
while no_atual is not None:
    st.write(f"Nome: {no_atual.nome} --- Número: {no_atual.numero}")
    no_atual = no_atual.proximo


with st.container():
    st.title("Agenda de Contatos")
    st.write('---')

with st.container():
    st.subheader("Adicionar novo contato:")
    nome = st.text_input("Nome:")
    numero = st.text_input("Número:", help="(00) 00000-0000")
    #categoria = st.selectbox("Categoria:", ["Familiares", "Amigos", "Conhecidos"])
    if st.button("Salvar"):
        lista_dupla.adicionar_no_final(nome, numero)
        st.success(f"Nome: {nome} | Número: {numero} registrado!")
        st.experimental_rerun()

with st.container():
    st.subheader("Remover contato:")
    nome_remove = st.text_input("Nome do contato a ser removido:")
    if st.button("Remover"):
        lista_dupla.remover_no_inicio(nome, numero)
        st.success(f"O contato de {nome} foi removido da sua Agenda!")

with st.container():
    opc = st.sidebar.selectbox("Outras opções:", ("Buscar contato", "Enviar email",))
    if opc == "Buscar contato":
        st.subheader("Buscar")
        st.text_input("Digite o nome de um contato para buscar:")
        if st.button("Buscar"):
            #CHAMADA DA FUNÇÃO DO JON
            st.success(f"O contato de nome com número numero foi encontrado!")





#codigo com armazenamento


'''import streamlit as st

class contato:
    def __init__(self, nome, numero):
        self.nome = nome
        self.numero = numero
        self.proximo = None
        self.anterior = None

class Listacontatos:
    def __init__(self):
        self.cabeca = None
        self.cauda = None

    def adicionar_no_final(self, nome, numero):
        novo_no = contato(nome, numero)
        if self.cabeca is None:
            self.cabeca = novo_no
            self.cauda = novo_no
        else:
            novo_no.anterior = self.cauda
            self.cauda.proximo = novo_no
            self.cauda = novo_no

def main():
    st.title("Lista de contatos")

    # Use o cache do Streamlit para persistir a lista dupla entre as chamadas
    @st.cache(allow_output_mutation=True)
    def obter_ou_criar_lista():
        return Listacontatos()

    lista_dupla = obter_ou_criar_lista()

    # Interface para adicionar dados à lista dupla
    novo_nome = st.text_input("Digite um novo nome:")
    novo_numero = st.text_input("Digite um novo numero:")
    if st.button("registrar"):
        lista_dupla.adicionar_no_final(novo_nome, novo_numero)
        st.success(f"({novo_nome}, {novo_numero}) registrado!")

    # Interface para exibir a lista dupla
    st.header("Contatos:")
    no_atual = lista_dupla.cabeca
    while no_atual is not None:
        st.write(f"Nome: {no_atual.nome}, Numero: {no_atual.numero}")
        no_atual = no_atual.proximo

if __name__ == "__main__":
    main()

'''




###################################################################################
#Ordenacao e busca prontos
"""import streamlit as st

class Contato:
    def __init__(self, nome, numero):
        self.nome = nome
        self.numero = numero
        self.proximo = None

class Listacontatos:
    def __init__(self):
        self.cabeca = None

    def adicionar_no_final(self, nome, numero):
        novo_no = Contato(nome, numero)
        if self.cabeca is None:
            self.cabeca = novo_no
        else:
            atual = self.cabeca
            while atual.proximo is not None:
                atual = atual.proximo
            atual.proximo = novo_no
        self.ordenar_contatos()

    def ordenar_contatos(self):
        if self.cabeca is None or self.cabeca.proximo is None:
            return

        no_atual = self.cabeca.proximo
        self.cabeca.proximo = None

        while no_atual is not None:
            no_seguinte = no_atual.proximo

            if no_atual.nome.lower() < self.cabeca.nome.lower():
                no_atual.proximo = self.cabeca
                self.cabeca = no_atual
            else:
                temp = self.cabeca
                while temp.proximo is not None and no_atual.nome.lower() > temp.proximo.nome.lower():
                    temp = temp.proximo
                no_atual.proximo = temp.proximo
                temp.proximo = no_atual

            no_atual = no_seguinte

    def busca_binaria(self, nome):
        inicio = 0
        fim = self.contar_contatos() - 1

        while inicio <= fim:
            meio = (inicio + fim) // 2
            posicao = 0
            atual = self.cabeca

            # Encontrar o meio na lista encadeada
            while posicao < meio:
                atual = atual.proximo
                posicao += 1

            # Verificar se o nome está no meio da lista
            if atual.nome.lower() == nome.lower():
                return atual
            elif atual.nome.lower() < nome.lower():
                inicio = meio + 1
            else:
                fim = meio - 1

        return None

    def contar_contatos(self):
        contador = 0
        atual = self.cabeca
        while atual:
            contador += 1
            atual = atual.proximo
        return contador

# Restante do seu código Streamlit permanece o mesmo...

st.set_page_config(page_title="Agenda de Contatos")


@st.cache(allow_output_mutation=True)
def obter_ou_criar_lista():
    return Listacontatos()

lista_dupla = obter_ou_criar_lista()

st.header("Sua Agenda de Contatos:")
no_atual = lista_dupla.cabeca
while no_atual is not None:
    st.write(f"Nome: {no_atual.nome} --- Número: {no_atual.numero}")
    no_atual = no_atual.proximo


with st.container():
    st.title("Agenda de Contatos")
    st.write('---')

with st.container():
    st.subheader("Adicionar novo contato:")
    nome = st.text_input("Nome:")
    numero = st.text_input("Número:", help="(00) 00000-0000")
    #categoria = st.selectbox("Categoria:", ["Familiares", "Amigos", "Conhecidos"])
    if st.button("Salvar"):
        lista_dupla.adicionar_no_final(nome, numero)
        st.success(f"Nome: {nome} | Número: {numero} registrado!")

with st.container():
    st.subheader("Remover contato:")
    nome_remove = st.text_input("Nome do contato a ser removido:")
    if st.button("Remover"):
        lista_dupla.remover_no_inicio(nome, numero)
        st.success(f"O contato de {nome} foi removido da sua Agenda!")

# Seu código anterior ...

with st.container():
    opc = st.sidebar.selectbox("Outras opções:", ("Buscar contato", "Enviar email",))
    if opc == "Buscar contato":
        st.subheader("Buscar")
        nome_busca = st.text_input("Digite o nome de um contato para buscar:")

        if st.button("Buscar"):
            nome_busca = nome_busca.strip().lower()  # Remover espaços extras e transformar em minúsculas
            resultado_busca = lista_dupla.busca_binaria(nome_busca)

            if resultado_busca:
                st.success(f"Contato encontrado - Nome: {resultado_busca.nome} | Número: {resultado_busca.numero}")
            else:
                st.error("Contato não encontrado.")
"""
