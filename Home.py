import streamlit as st
import pandas as pd
import security.segredos as ss
from PIL import Image

st.sidebar.header("Faça se Login abaixo")
# Lista de usuários e senhas
user_pwd = ss.usuarios_e_senhas

# Função para autenticar o usuário
def autenticar_usuario(usuario, senha):
    senha_correta = user_pwd.get(usuario)
    if senha_correta == senha:
        return True
    return False

# Criar uma interface de login com Streamlit
# Campos de entrada para nome de usuário e senha
usuario = st.sidebar.text_input("Usuário")
senha = st.sidebar.text_input("Senha", type="password")

# Botão de login
if st.sidebar.checkbox("Entrar"):
    if autenticar_usuario(usuario, senha):
        st.sidebar.success("Login bem-sucedido!")
        cabecalho = ('Relatório de Visitas')
        titulo = Image.open('Logo_Telefonica2.png')
        cliente = st.text_input('Cliente')
        tipo = st.selectbox("Selecione o Tipo de Manutenção",["Preventiva","Corretiva"])
        tecnico1 = st.text_input('Nome do Técnico 1')
        tecnico2 = st.text_input('Nome do Técnico 2')
        data = st.date_input('Digite a Data')
        h_inicio = st.time_input('Hora Inicial')
        h_final = st.time_input('Hora Final')
        descricao = st.text_area('Descrição do Serviço')
        imagem = st.file_uploader("Faça o upload das imagens (JPEG ou PNG)", type=["jpg", "jpeg", "png"], accept_multiple_files=True)
        if st.button('Mostrar Relatorio'):
            st.image(titulo)
            st.header(cabecalho)
            st.caption(f':blue[Cliente]: {cliente.upper()}')
            if tipo:
                st.write(f':blue[Tipo de Manutenção]: {tipo}')
            st.caption(f':blue[Técnico 1]: {tecnico1.upper()}')
            st.caption(f':blue[Técnico 2]: {tecnico2.upper()}')
            st.caption(f':blue[Data]: {data}')
            st.caption(f':blue[Hora Inicial do Atendimento]: {h_inicio}')
            st.caption(f':blue[Hora Final do Atendimento]: {h_final}')
            st.caption(f':blue[Dercição dos serviços Executados]: {descricao.upper()}')
            if imagem:
                st.image(imagem)
    else:
        st.error("Credenciais incorretas. Tente novamente.")
        
