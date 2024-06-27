import pandas as pd
import os
import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
from datetime import datetime

clientes_csv_file = 'clientes.csv' # variavel de caminho do arquivo CSV

def valor_plano(tipo): # Fução para definir Valor do Plano | Retona o preço
    if tipo == "Básico":
        preco = 99.90
    elif tipo == "Intermediário":
        preco = 199.90
    elif tipo == "Premium":
        preco = 299.90
    return preco

def init_csv_files(): # Função para inicializar os CSVs
    if not os.path.exists(clientes_csv_file):
        clientes_df = pd.DataFrame(columns=["Nome", "Plano", "Preço", "Data de Matrícula", "Username", "Role", "Password"])
        clientes_df.to_csv(clientes_csv_file, index=False)

init_csv_files() # Inicializar os arquivos CSV

def read_clientes_csv(): # Ler cliente.csv
    return pd.read_csv(clientes_csv_file)

def save_clientes_csv(df): # Salva cliente.csv | Salva atualizações
    df.to_csv(clientes_csv_file, index=False)

def read_user(): # Ler arquivo config.yaml | Retornas dataframes
    with open("config.yaml", 'r') as file:
        config = yaml.safe_load(file)
        return config

def read_treino(treino):  # Ler arquivo CSV | Retornas dataframes
    treino = treino.lower()
    file_path = f"treinos/{treino}.csv"
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        st.error(f"Selecione um plano de treino.")
        return pd.DataFrame(columns=["Exercício", "Séries", "Repetições", "Descanso(segundos)"])
    
def save_user(): # Salva Arquivo config.yaml | Salva atualizações
    with open("config.yaml", 'w') as file:
        yaml.dump(config, file, default_flow_style=False)

def create_cliente(nome, plano, password, data_matricula=datetime.today().date()): # Cria um cliente
    
    df = read_clientes_csv()
    username = nome.split()[0].lower()  # Usar apenas o primeiro nome como username
    new_cliente = {"Nome": nome, "Plano": plano, "Preço": valor_plano(plano), "Data de Matrícula": data_matricula, "Username": username, "Role": "Cliente", "Password": password}
        
    # Criar um novo DataFrame com a nova linha adicionada
    df = pd.concat([df, pd.DataFrame([new_cliente])], ignore_index=True)
        
    save_clientes_csv(df)
    st.success(f"Cliente {nome} adicionado com sucesso.")

def read_clientes(name=None, plano=None): # Ler clientes
    df = read_clientes_csv()
    # Verificar se ambos name e plano são None
    if not name and not plano:
        st.error("Por favor, forneça um nome ou um plano para a pesquisa.")
        return
    # Filtrar por nome se fornecido
    if name:
        df = df[df['Nome'].str.contains(name, case=False, na=False)]
    # Filtrar por plano se fornecido
    if plano:
        df = df[df['Plano'].str.contains(plano, case=False, na=False)]
    # Exibir os resultados
    if not df.empty:
        st.dataframe(df)
    else:
        st.error("Nenhum cliente encontrado com os critérios fornecidos.")

def update_cliente(nome, novo_plano=None): # Update: Atualizar dados de um cliente pelo nome
        df = read_clientes_csv()
        if nome in df["Nome"].values:
            if novo_plano:
                df.loc[df["Nome"] == nome, "Plano"] = novo_plano
                df.loc[df["Nome"] == nome, "Preço"] = valor_plano(novo_plano)
            save_clientes_csv(df)
            st.success(f"Cliente {nome} atualizado com sucesso.")
        else:
            st.error(f"Cliente {nome} não encontrado.")

def delete_cliente(nome): # Remove um cliente pelo nome
    df = read_clientes_csv()
    if nome in df["Nome"].values:
        df = df[df["Nome"] != nome]
        save_clientes_csv(df)
        st.success(f"Cliente {nome} removido com sucesso.")
    else:
        st.error(f"Cliente {nome} não encontrado. Digite o nome completo como no cadastro!")

def create_user(username, email, name, password, role): # Cria um usuario
    read_user()
    # Verificar se as seções 'credentials' e 'usernames' existem
    if 'credentials' not in config:
        config['credentials'] = {}
    if 'usernames' not in config['credentials']:
        config['credentials']['usernames'] = {}
    # Verificar se o usuário já existe
    if username in config['credentials']['usernames']:
        st.error(f"Erro: Usuário {username} já existe.")
    else:
        # Adicionar o novo usuário ao dicionário de usernames
        config['credentials']['usernames'][username] = {
            'email': email,
            'logged_in': False,
            'name': name,
            'password': password,
            'role': role
        }
        save_user()
        st.success(f"Usuário {username} adicionado com sucesso.")

def view_user(username=None, role=None):
    read_user()

    if 'credentials' in config and 'usernames' in config['credentials']:
        users = config['credentials']['usernames']
        # Converte o dicionário em um DataFrame para facilitar a filtragem
        df = pd.DataFrame(users).T.reset_index().rename(columns={'index': 'Username'})
        # Verificar se ambos username e role são None
        if not username and not role:
            st.error("Por favor, forneça um nome de usuário ou um papel para a pesquisa.")
            return
        # Filtrar por username se fornecido
        if username:
            df = df[df['Username'].str.contains(username, case=False, na=False)]   
        # Filtrar por role se fornecido
        if role:
            df = df[df['role'].str.contains(role, case=False, na=False)]
        # Exibir os resultados
        if not df.empty:
            st.dataframe(df)
        else:
            st.error("Nenhum usuário encontrado com os critérios fornecidos.")
    else:
        st.error("Nenhum usuário encontrado.")

def update_user(username, new_email=None, new_name=None, new_password=None, new_role=None, file_path='config.yaml'): # Função para atualizar dados de um usuário
    read_user()
    
    if 'credentials' in config and 'usernames' in config['credentials'] and username in config['credentials']['usernames']:
        if new_email:
            config['credentials']['usernames'][username]['email'] = new_email
        if new_name:
            config['credentials']['usernames'][username]['name'] = new_name
        if new_password:
            config['credentials']['usernames'][username]['password'] = new_password
        if new_role:
            config['credentials']['usernames'][username]['role'] = new_role
        
        save_user()
        st.success(f"Usuário {username} atualizado com sucesso.")
    else:
        st.error(f"Usuário {username} não encontrado.")
        
def delete_user(username): # Deleta um usuário
    read_user()
    if 'credentials' in config and 'usernames' in config['credentials'] and username in config['credentials']['usernames']:
        del config['credentials']['usernames'][username]
        save_user()
        st.success(f"Usuário {username} removido com sucesso.")
    else:
        st.error(f"Usuário {username} não encontrado.")

def admin_page(): # Página de Administrador
    
    with st.sidebar:
        st.image("imgs/logo.png")
        st.header("Painel do Administrador")
        st.subheader("Bem-vindo, " + st.session_state["name"] + "!")

        st.subheader("Gerenciamento de Clientes")
        option = st.sidebar.selectbox("Escolha uma ação", ["Adicionar Cliente", "Visualizar Clientes", "Atualizar Cliente", "Deletar Cliente"])
        toogle_cliente = st.toggle("Ativar Grenciamento de Clientes", key="clientes")

        st.subheader("Gerenciamento de Usuários")
        user_option = st.selectbox("Escolha uma ação", ["Adicionar Usuário", "Visualizar Usuário", "Atualizar Usuário", "Deletar Usuário"])
        toggle_user = st.toggle("Ativar Grenciamento de Usuarios", key="user")
        authenticator.logout()

    if toogle_cliente:
        st.subheader("Gerenciamento de Clientes")
        if option == "Adicionar Cliente":
            st.subheader("Adicionar Cliente")
            nome = st.text_input("Nome")
            plano = st.selectbox("Plano", ["Básico", "Intermediário", "Premium"])
            password = st.text_input("Password", type="password")
            if st.button("Adicionar Cliente"):
                create_cliente(nome, plano, password)

        elif option == "Atualizar Cliente":
            st.subheader("Atualizar Cliente")
            nome = st.text_input("Nome do Cliente")
            novo_plano = st.selectbox("Novo Plano", ["Básico", "Intermediário", "Premium"])
            if st.button("Atualizar Cliente"):
                update_cliente(nome, novo_plano)

        elif option == "Deletar Cliente":
            st.subheader("Deletar Cliente")
            nome = st.text_input("Nome do Cliente")
            if st.button("Pesquisar"):
                read_clientes(nome)
            if st.button("Deletar Cliente"):
                delete_cliente(nome)

        elif option == "Visualizar Clientes":
            st.subheader("Pesquisar Cliente")

            nome = st.text_input("Nome do Cliente")
            plano = st.selectbox("Plano", ["", "Básico", "Intermediário", "Premium"])
            if st.button("Pesquisar"):
                read_clientes(nome, plano)

    if toggle_user:
        st.subheader("Gerenciamento de Usuários")

        if user_option == "Adicionar Usuário":
            username = st.text_input("Nome de Usuário")
            name = st.text_input("Name")
            email = st.text_input("Email")
            role = st.selectbox("Role", ["admin", "view", "customer"])
            password = st.text_input("Password")
            if st.button("Adicionar Usuário"):
                create_user(username, email, name, password, role)

        elif user_option == "Deletar Usuário":
            username = st.text_input("Username")
            if st.button("Deletar Usuário"):
                delete_user(username)

        elif user_option == "Visualizar Usuário":
            username_filter = st.text_input("Nome de Usuário")
            role_filter = st.text_input("Papel do Usuário")
            if st.button("Pesquisar Usuários"):
                view_user(username_filter, role_filter)

        elif user_option == "Atualizar Usuário":
            username = st.text_input("Nome de Usuário para Atualizar")
            new_email = st.text_input("Novo Email")
            new_name = st.text_input("Novo Nome")
            new_password = st.text_input("Nova Senha")
            new_role = st.selectbox("Novo Papel", ["", "admin", "view", "customer"])
            if st.button("Atualizar Usuário"):
                update_user(username, new_email, new_name, new_password, new_role)

def viewer_page(): # Página de Visualizador
    
    with st.sidebar:
        st.image("imgs/logo.png")
        st.header("Área do Visualizador")
        st.subheader("Bem-vindo, " + st.session_state["name"] + "!")
        
        st.header("Pesquisar Cliente")
        
        nome = st.text_input("Nome do Cliente")
        plano = st.selectbox("Plano", ["", "Básico", "Intermediário", "Premium"])
        search_button = st.sidebar.button("Pesquisar")
        authenticator.logout()

    
    if search_button:

        read_clientes(nome, plano)

def client_page(): # Página de Cliente
    with st.sidebar:
        st.image("imgs/logo.png")
        st.header("Área do Cliente")
        st.subheader("Bem-vindo, " + st.session_state["name"] + "!")
        treino = st.selectbox("Selecione seu treino", ["","ABS", "Costas", "Peito", "Perna"])
        authenticator.logout()

    st.subheader(f"Treino de {treino}")
    st.dataframe(read_treino(treino))

    st.write("Em breve com mais atualizações....")

# Configurações de Paginas e Login Streamlit e Streamlit Authenticator

st.set_page_config(
    page_title="Desenvolve Academia",
    page_icon="imgs/flaticon.png",
    initial_sidebar_state="expanded")

with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['pre-authorized']
)

name, authentication_status, username  = authenticator.login(fields=['username', 'password'])

if authentication_status: # Separaçao dos usuarios pelas suas permissões no role do credential dentro do config.yaml
    user_role = config['credentials']['usernames'][username]['role']
    # Verificar o role e exibir o conteúdo apropriado
    if user_role == 'admin':
        st.header('Painel do Admin')
        admin_page()
    elif user_role == 'view':
        st.header('Painel do Visualizador')
        viewer_page()
    elif user_role == 'customer':
        st.header('Painel do Cliente')
        client_page()
elif authentication_status == False:
    st.error('Username/password is incorrect')
elif authentication_status == None:
    st.warning('Please enter your username and password')
    