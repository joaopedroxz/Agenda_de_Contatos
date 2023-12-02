#QUASE PRONTO COM ICONE DO WPP

import time
import streamlit as st
#from awesome_streamlit.shared.components import awesome_icons

class Contato:
    def __init__(self, nome, numero):
        self.nome = nome
        self.numero = numero
        self.anterior = None
        self.proximo = None


class Listacontatos:
    def __init__(self):
        self.cabeca = None
        self.cauda = None

    def adicionar_contato(self, nome, numero):
        if self.busca_binaria(nome):
            st.warning("Este contato já existe na sua Agenda!")
            return
        novo_contato = Contato(nome, numero)
        if self.cauda is None:
            self.cabeca = novo_contato
            self.cauda = novo_contato
        else:
            novo_contato.anterior = self.cauda
            self.cauda.proximo = novo_contato
            self.cauda = novo_contato
        self.ordenar_contatos()

    def mover_remover(self, nome):
        atual = self.cabeca

        while atual:

            if atual.nome == nome:
                if atual == self.cabeca:
                    return self.apagar_primeiro_contato()

                anterior = atual.anterior
                proximo = atual.proximo

                if anterior:
                    anterior.proximo = proximo
                else:
                    self.cabeca = proximo

                if proximo:
                    proximo.anterior = anterior
                else:
                    self.cauda = anterior

                atual.proximo = self.cabeca
                atual.anterior = None
                self.cabeca.anterior = atual
                self.cabeca = atual

                return self.apagar_primeiro_contato()

            if atual.proximo == None:
                print("Não encontrado")
                return
            atual = atual.proximo

    def apagar_primeiro_contato(self):
        if self.cabeca is None:
            return

        primeiro_contato = self.cabeca
        self.cabeca = primeiro_contato.proximo

        if self.cabeca:
            self.cabeca.anterior = None
        else:
            self.cauda = None

        del primeiro_contato



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
def validador_nome(nome):
    if len(nome) > 0:
        return nome
def validador_numero(numero):
    if len(numero) == 11:
        return numero

st.set_page_config(page_title="Agenda de Contatos")

def obter_ou_criar_lista():
    if "lista_dupla" not in st.session_state:
        st.session_state.lista_dupla = Listacontatos()
    return st.session_state.lista_dupla

# Função para exibir a lista de contatos

def display_contact_list():
    st.header("Sua Agenda de Contatos:")
    lista_dupla = obter_ou_criar_lista()
    contato_atual = lista_dupla.cabeca
    while contato_atual is not None:
        st.write(f"Nome: {contato_atual.nome}")
        st.write(f"Número: {contato_atual.numero}")
        st.write("---")
        contato_atual = contato_atual.proximo



with st.container():
    st.title("Agenda de Contatos")
    st.write('---')

with st.container():
    st.subheader("Adicionar novo contato:")
    nome = st.text_input("Nome:")
    numero = st.text_input("Número:", help="(00) 00000-0000")
    if validador_nome(nome) and validador_numero(numero):
        if st.button("Salvar", key="salvar_contato"):
            lista_dupla = obter_ou_criar_lista()
            lista_dupla.adicionar_contato(nome, numero)
            st.success(f"O contato de  {nome} com número {numero} foi registrado!")
            #st.empty()
            #st.experimental_rerun()
    else:
        st.warning("Por favor, digite o nome do contato e o número com 11 dígitos!")

with st.container():
    st.subheader("Remover contato:")
    nome_remove = st.text_input("Nome do contato a ser removido:")
    if validador_nome(nome_remove):
        if st.button("Remover", key="remover_contato"):
            lista_dupla = obter_ou_criar_lista()
            lista_dupla.mover_remover(nome_remove)
            st.success(f"O contato de {nome_remove} foi removido da sua Agenda!")
        else:
            st.error("O contato não foi encontrado na sua Agenda")
            #st.experimental_rerun()
    else:
        st.warning("Digite um nome para ser removido")
with st.container():
    opc = st.sidebar.selectbox("Outras opções:", ("Home", "Buscar contato",))
    if opc == "Buscar contato":
        st.subheader("Buscar")
        nome_busca = st.text_input("Digite o nome de um contato para buscar:")
        if st.button("Buscar"):
            lista_dupla = obter_ou_criar_lista()
            nome_busca = nome_busca.strip().lower()  # Remover espaços extras e transformar em minúsculas
            resultado_busca = lista_dupla.busca_binaria(nome_busca)
            if resultado_busca:
                st.success(f"Contato encontrado\n- Nome: {resultado_busca.nome}\n- Número: {resultado_busca.numero}")
                st.write("Opções:")
                url_whatsapp = f"https://wa.me/{resultado_busca.numero}"
                st.markdown('<i class="fab fa-whatsapp" style="font-size: 2em;"></i>', unsafe_allow_html=True)
                st.markdown('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">',unsafe_allow_html=True)
                st.link_button('Encaminhar para o Whatsapp', url_whatsapp, help="Abrir Whatsapp")
                #st.link_button('Enviar um email')

            else:
                st.error("Contato não encontrado.")


if st.sidebar.button('Atualizar página'):
    with st.spinner("Atualizando..."):
        time.sleep(2)
        st.experimental_rerun()
        st.empty()



display_contact_list()

##########################################################################################################################################################
#CÓDIGO QUASE PRONTO
import time
import streamlit as st
#from awesome_streamlit.shared.components import awesome_icons

class Contato:
    def __init__(self, nome, numero):
        self.nome = nome
        self.numero = numero
        self.anterior = None
        self.proximo = None


class Listacontatos:
    def __init__(self):
        self.cabeca = None
        self.cauda = None

    def adicionar_contato(self, nome, numero):
        if self.busca_binaria(nome):
            st.warning("Este contato já existe na sua Agenda!")
            return
        novo_contato = Contato(nome, numero)
        if self.cauda is None:
            self.cabeca = novo_contato
            self.cauda = novo_contato
        else:
            novo_contato.anterior = self.cauda
            self.cauda.proximo = novo_contato
            self.cauda = novo_contato
        self.ordenar_contatos()

    def mover_remover(self, nome):
        atual = self.cabeca

        while atual:

            if atual.nome == nome:
                if atual == self.cabeca:
                    return self.apagar_primeiro_contato()

                anterior = atual.anterior
                proximo = atual.proximo

                if anterior:
                    anterior.proximo = proximo
                else:
                    self.cabeca = proximo

                if proximo:
                    proximo.anterior = anterior
                else:
                    self.cauda = anterior

                atual.proximo = self.cabeca
                atual.anterior = None
                self.cabeca.anterior = atual
                self.cabeca = atual

                return self.apagar_primeiro_contato()

            if atual.proximo == None:
                print("Não encontrado")
                return
            atual = atual.proximo

    def apagar_primeiro_contato(self):
        if self.cabeca is None:
            return

        primeiro_contato = self.cabeca
        self.cabeca = primeiro_contato.proximo

        if self.cabeca:
            self.cabeca.anterior = None
        else:
            self.cauda = None

        del primeiro_contato



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
def validador_nome(nome):
    if len(nome) > 0:
        return nome
def validador_numero(numero):
    if len(numero) == 11:
        return numero

st.set_page_config(page_title="Agenda de Contatos")

def obter_ou_criar_lista():
    if "lista_dupla" not in st.session_state:
        st.session_state.lista_dupla = Listacontatos()
    return st.session_state.lista_dupla

# Função para exibir a lista de contatos

def display_contact_list():
    st.header("Sua Agenda de Contatos:")
    lista_dupla = obter_ou_criar_lista()
    contato_atual = lista_dupla.cabeca
    while contato_atual is not None:
        st.write(f"Nome: {contato_atual.nome}")
        st.write(f"Número: {contato_atual.numero}")
        st.write("---")
        contato_atual = contato_atual.proximo



with st.container():
    st.title("Agenda de Contatos")
    st.write('---')

with st.container():
    st.subheader("Adicionar novo contato:")
    nome = st.text_input("Nome:")
    numero = st.text_input("Número:", help="(00) 00000-0000")
    if validador_nome(nome) and validador_numero(numero):
        if st.button("Salvar", key="salvar_contato"):
            lista_dupla = obter_ou_criar_lista()
            lista_dupla.adicionar_contato(nome, numero)
            st.success(f"O contato de  {nome} com número {numero} foi registrado!")
            #st.empty()
            #st.experimental_rerun()
    else:
        st.warning("Por favor, digite o nome do contato e o número com 11 dígitos!")

with st.container():
    st.subheader("Remover contato:")
    nome_remove = st.text_input("Nome do contato a ser removido:")
    if validador_nome(nome_remove):
        if st.button("Remover", key="remover_contato"):
            lista_dupla = obter_ou_criar_lista()
            lista_dupla.mover_remover(nome_remove)
            st.success(f"O contato de {nome_remove} foi removido da sua Agenda!")
        else:
            st.error("O contato não foi encontrado na sua Agenda")
            #st.experimental_rerun()
    else:
        st.warning("Digite um nome para ser removido")
with st.container():
    opc = st.sidebar.selectbox("Outras opções:", ("Home", "Buscar contato",))
    if opc == "Buscar contato":
        st.subheader("Buscar")
        nome_busca = st.text_input("Digite o nome de um contato para buscar:")
        if st.button("Buscar"):
            lista_dupla = obter_ou_criar_lista()
            nome_busca = nome_busca.strip().lower()  # Remover espaços extras e transformar em minúsculas
            resultado_busca = lista_dupla.busca_binaria(nome_busca)
            if resultado_busca:
                st.success(f"Contato encontrado\n- Nome: {resultado_busca.nome}\n- Número: {resultado_busca.numero}")
                st.write("Opções:")
                url_whatsapp = f"https://wa.me/{resultado_busca.numero}"
                st.link_button('Encaminhar para o Whatsapp', url_whatsapp, help="Abrir Whatsapp")
                #st.link_button('Enviar um email')

            else:
                st.error("Contato não encontrado.")


if st.sidebar.button('Atualizar página'):
    with st.spinner("Atualizando..."):
        time.sleep(2)
        st.experimental_rerun()
        st.empty()



display_contact_list()









########################################################################################################################################################
#codigo que aparentemente deu certo
import streamlit as st

class Contato:
    def __init__(self, nome, numero):
        self.nome = nome
        self.numero = numero
        self.anterior = None
        self.proximo = None

class Listacontatos:
    def __init__(self):
        self.cabeca = None
        self.cauda = None

    def adicionar_contato(self, nome, numero):
        novo_contato = Contato(nome, numero)

        if self.cauda is None:
            self.cabeca = novo_contato
            self.cauda = novo_contato
        else:
            novo_contato.anterior = self.cauda
            self.cauda.proximo = novo_contato
            self.cauda = novo_contato
        self.ordenar_contatos()

    def mover_remover(self, nome):
        atual = self.cabeca

        while atual:

            if atual.nome == nome:
                if atual == self.cabeca:
                    return self.apagar_primeiro_contato()

                anterior = atual.anterior
                proximo = atual.proximo

                if anterior:
                    anterior.proximo = proximo
                else:
                    self.cabeca = proximo

                if proximo:
                    proximo.anterior = anterior
                else:
                    self.cauda = anterior

                atual.proximo = self.cabeca
                atual.anterior = None
                self.cabeca.anterior = atual
                self.cabeca = atual

                return self.apagar_primeiro_contato()

            if atual.proximo == None:
                print("Não encontrado")
                return
            atual = atual.proximo

    def apagar_primeiro_contato(self):
        if self.cabeca is None:
            return

        primeiro_contato = self.cabeca
        self.cabeca = primeiro_contato.proximo

        if self.cabeca:
            self.cabeca.anterior = None
        else:
            self.cauda = None

        del primeiro_contato



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
contato_atual = lista_dupla.cabeca
while contato_atual is not None:
    st.write(f"Nome: {contato_atual.nome} --- Número: {contato_atual.numero}")
    contato_atual = contato_atual.proximo


with st.container():
    st.title("Agenda de Contatos")
    st.write('---')

with st.container():
    st.subheader("Adicionar novo contato:")
    nome = st.text_input("Nome:")
    numero = st.text_input("Número:", help="(00) 00000-0000")
    #categoria = st.selectbox("Categoria:", ["Familiares", "Amigos", "Conhecidos"])
    if st.button("Salvar"):
        lista_dupla.adicionar_contato(nome, numero)
        st.success(f"Nome: {nome} | Número: {numero} registrado!")

with st.container():
    st.subheader("Remover contato:")
    nome_remove = st.text_input("Nome do contato a ser removido:")
    if st.button("Remover"):
        lista_dupla.mover_remover(nome_remove)
        st.success(f"O contato de {nome_remove} foi removido da sua Agenda!")

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



#=============================================================================================================
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
################################################################################################################################################
###############################################################################################################################################
###############################################################################################################################################
ESSE AQUI 
import streamlit as st


# from awesome_streamlit.shared.components import awesome_icons

class Contato:
    def __init__(self, nome, numero):
        self.nome = nome
        self.numero = numero
        self.anterior = None
        self.proximo = None


class Listacontatos:
    def __init__(self):
        self.cabeca = None
        self.cauda = None

    # para seguir o comportamento de uma fila, vamos adionar ao final e remover no inicio

    # adiciona dados no final da lista
    def adicionar_contato(self, nome, numero):
        novo_contato = Contato(nome, numero)

        if self.cabeca is None:
            self.cabeca = novo_contato
            self.cauda = novo_contato
        else:
            self.cauda.proximo = novo_contato
            novo_contato.anterior = self.cauda
            self.cauda = novo_contato
        self.ordenar_contatos()

    # move o contato escolhido para a cabeca e chama função para remover
    def mover_remover(self, nome):
        atual = self.cabeca

        while atual:

            if atual.nome == nome:
                if atual == self.cabeca:
                    return self.apagar_primeiro_contato()

                anterior = atual.anterior
                proximo = atual.proximo

                if anterior:
                    anterior.proximo = proximo
                else:
                    self.cabeca = proximo

                if proximo:
                    proximo.anterior = anterior
                else:
                    self.cauda = anterior

                atual.proximo = self.cabeca
                atual.anterior = None
                self.cabeca.anterior = atual
                self.cabeca = atual

                return self.apagar_primeiro_contato()

            if atual.proximo == None:
                print("Não encontrado")
                return
            atual = atual.proximo

    # apaga o primeiro contato
    def apagar_primeiro_contato(self):
        if self.cabeca is None:
            return

        primeiro_contato = self.cabeca
        self.cabeca = primeiro_contato.proximo

        if self.cabeca:
            self.cabeca.anterior = None
        else:
            self.cauda = None

        del primeiro_contato

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


def validador_nome(nome):
    if len(nome) > 0:
        return nome


def validador_numero(numero):
    if len(numero) == 11:
        return numero


st.set_page_config(page_title="Agenda de Contatos")


def obter_ou_criar_lista():
    if "lista_dupla" not in st.session_state:
        st.session_state.lista_dupla = Listacontatos()
    return st.session_state.lista_dupla


# Função para exibir a lista de contatos

def display_contact_list():
    st.header("Sua Agenda de Contatos:")
    lista_dupla = obter_ou_criar_lista()
    contato_atual = lista_dupla.cabeca
    while contato_atual is not None:
        st.write(f"Nome: {contato_atual.nome}")
        st.write(f"Número: {contato_atual.numero}")
        st.write("---")
        contato_atual = contato_atual.proximo


with st.container():
    st.title("Agenda de Contatos")
    st.write('---')

with st.container():
    st.subheader("Adicionar novo contato:")
    nome = st.text_input("Nome:")
    numero = st.text_input("Número:", help="(00) 00000-0000")
    if validador_nome(nome) and validador_numero(numero):
        if st.button("Salvar", key="salvar_contato"):
            lista_dupla = obter_ou_criar_lista()
            lista_dupla.adicionar_contato(nome, numero)
            st.success(f"O contato de  {nome} com número {numero} foi registrado!")
            # st.empty()
            # st.experimental_rerun()
    else:
        st.warning("Por favor, digite o nome do contato e o número com 11 dígitos!")

with st.container():
    st.subheader("Remover contato:")
    nome_remove = st.text_input("Nome do contato a ser removido:")
    if validador_nome(nome_remove):
        if st.button("Remover", key="remover_contato"):
            lista_dupla = obter_ou_criar_lista()
            lista_dupla.mover_remover(nome_remove)
            st.success(f"O contato de {nome_remove} foi removido da sua Agenda!")
        else:
            st.error("O contato não foi encontrado na sua Agenda")
            # st.experimental_rerun()
    else:
        st.warning("Digite um nome para ser removido")
with st.container():
    opc = st.sidebar.selectbox("Outras opções:", ("Home", "Buscar contato",))
    if opc == "Buscar contato":
        st.subheader("Buscar")
        nome_busca = st.text_input("Digite o nome de um contato para buscar:")
        if st.button("Buscar"):
            lista_dupla = obter_ou_criar_lista()
            nome_busca = nome_busca.strip().lower()  # Remover espaços extras e transformar em minúsculas
            resultado_busca = lista_dupla.busca_binaria(nome_busca)
            if resultado_busca:
                st.success(f"Contato encontrado\n- Nome: {resultado_busca.nome}\n- Número: {resultado_busca.numero}")
                st.write("Opções:")
                url_whatsapp = f"https://wa.me/{resultado_busca.numero}"
                st.markdown(f"[Encaminhar para o WhatsApp]({url_whatsapp})", help="Abrir Whatsapp")

            else:
                st.error("Contato não encontrado.")

# st.sidebar.header("Configurações")
# user_input = st.sidebar.text_input("Digite algo:")


display_contact_list()
