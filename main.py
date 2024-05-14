# Dicionário de exemplo com usuários e senhas
usuarios = {
    "nelson": "1234",
    "max": "4321",
}

def verificar_credenciais(usuario, senha):
    """Verifica se as credenciais são válidas."""
    if usuario in usuarios and usuarios[usuario] == senha:
        #esse True vai aparecer na linha 29 se o teste der verdadeiro
        return True
    else:
        #raise é a função que indica que ocorreu um erro 
        raise ValueError("Nome de usuário ou senha incorretos.")

def login():
    while True:
        try:
            # Solicita ao usuário que insira o nome de usuário e a senha
            usuario = input("Digite seu nome de usuário (ou digite 'sair' para encerrar): ")
            if usuario.lower() == 'sair':
                print("Encerrando o programa.")
                break

            senha = input("Digite sua senha: ")

            # Verifica as credenciais
            if verificar_credenciais(usuario, senha):
                print(f"Login bem-sucedido. Bem-vindo, {usuario}!")
                break
        except ValueError as e:
            # Captura exceções ValueError relacionadas a credenciais inválidas
            print(e)
        else:
            # Executado apenas se o bloco try for bem-sucedido
            print("Você está logado com sucesso.")
        finally:
            # Executado independentemente de uma exceção ter ocorrido ou não
            print("Tentativa de login finalizada.\n")

# Chama a função de login
login()
