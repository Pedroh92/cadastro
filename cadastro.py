
usuarios = []

def cadastrar_usuario():

    """
    Cadastra um novo usuário com nome, e-mail e idade.

    Pede ao usuário que digite nome, e-mail e idade e armazena as informações
    em um dicionário. Adiciona o dicionário à lista de usuários e imprime
    uma mensagem de sucesso.
    """

    

    
    

    nome = input("Digite o nome do usuário: ").strip()
    email = input("Digite o e-mail do usuário: ").strip()
    idade = input("Digite a idade do usuário: ").strip()

    usuario = {
        "nome": nome,
        "email": email,
        "idade": idade
    }
    usuarios.append(usuario)
    print("\nUsuário cadastrado com sucesso!\n")

def listar_usuarios():
    if not usuarios:
        print("\nNenhum usuário cadastrado.\n")
    else:
        print("\nLista de usuários cadastrados:")
        for idx, usuario in enumerate(usuarios, 1):
            print(f"{idx}. Nome: {usuario['nome']} | E-mail: {usuario['email']} | Idade: {usuario['idade']}")
        print()

def buscar_usuario():

    """
    Busca um usuário pelo nome.

    Pede ao usuário que digite o nome do usuário que deseja buscar e
    imprime as informações do usuário encontrado ou uma mensagem de
    erro caso o usuário não seja encontrado.
    """




    nome_busca = input("Digite o nome do usuário que deseja buscar: ").strip().lower()
    encontrados = [u for u in usuarios if u['nome'].lower() == nome_busca]

    if encontrados:
        print("\nUsuário(s) encontrado(s):")
        for usuario in encontrados:
            print(f"Nome: {usuario['nome']} | E-mail: {usuario['email']} | Idade: {usuario['idade']}")
    else:
        print("\nNenhum usuário encontrado com esse nome.")
    print()

def menu():

    """
    Mostra o menu de opções ao usuário e executa a ação escolhida.

    Opções:
    1. Cadastrar usuário
    2. Listar usuários
    3. Buscar usuário por nome
    4. Sair

    Se a opção for inválida, exibe mensagem de erro e volta ao menu.
    """

    while True:
        print("==== MENU ====")
        print("1. Cadastrar usuário")
        print("2. Listar usuários")
        print("3. Buscar usuário por nome")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastrar_usuario()
        elif opcao == '2':
            listar_usuarios()
        elif opcao == '3':
            buscar_usuario()
        elif opcao == '4':
            print("Encerrando aplicação. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.\n")

# Executar o menu
menu()