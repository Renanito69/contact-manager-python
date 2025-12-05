import os


def adicionar_contatos(lista_contatos):
    os.system('cls')
    print("Adicinando contato")
    contato = dict()
    contato['nome'] = str(input("Nome: ")).title()
    while True:
        try:
            contato['telefone'] = int(input("Numero: "))
            break
        except ValueError:
            print("Digite apenas numeros!")
    print("\nContato adicionado na lista")
    perguntar_e_limpar()
    lista_contatos.append(contato)


def listar_contato(lista_Contatos):
    os.system('cls')
    for pos, contato in enumerate(lista_Contatos):
        print(f"{pos+1} - {contato['nome']} -> {contato['telefone']}")


def perguntar_e_limpar():
    input("\nDigite uma tecla para voltar para o menu: ")
    os.system("cls")


def remover_contato(lista_Contatos):
    listar_contato(lista_Contatos)
    contato = int(
        input("Digite qual a posição do contato que deseja remover: "))
    print(
        f"\nO Contato {lista_Contatos[contato-1]['nome']} foi removido da lista")
    lista_Contatos.pop(contato-1)
    perguntar_e_limpar()


def buscar_contato(lista_Contatos):
    os.system('cls')
    buscar_contato_lista = str(input("Buscar Contato: ")).title()
    contatos_encontrados = 0
    for contato in lista_Contatos:
        if buscar_contato_lista in contato['nome']:
            print(f"{contato['nome']} -> {contato['telefone']}")
            contatos_encontrados += 1
    if contatos_encontrados == 0:
        print("Nenhum contato encontrado")
    perguntar_e_limpar()


def titulo():
    print("""
░█████╗░░██████╗░███████╗███╗░░██╗██████╗░░█████╗░  ██████╗░███████╗
██╔══██╗██╔════╝░██╔════╝████╗░██║██╔══██╗██╔══██╗  ██╔══██╗██╔════╝
███████║██║░░██╗░█████╗░░██╔██╗██║██║░░██║███████║  ██║░░██║█████╗░░
██╔══██║██║░░╚██╗██╔══╝░░██║╚████║██║░░██║██╔══██║  ██║░░██║██╔══╝░░
██║░░██║╚██████╔╝███████╗██║░╚███║██████╔╝██║░░██║  ██████╔╝███████╗
╚═╝░░╚═╝░╚═════╝░╚══════╝╚═╝░░╚══╝╚═════╝░╚═╝░░╚═╝  ╚═════╝░╚══════╝

░█████╗░░█████╗░███╗░░██╗████████╗░█████╗░████████╗░█████╗░░██████╗
██╔══██╗██╔══██╗████╗░██║╚══██╔══╝██╔══██╗╚══██╔══╝██╔══██╗██╔════╝
██║░░╚═╝██║░░██║██╔██╗██║░░░██║░░░███████║░░░██║░░░██║░░██║╚█████╗░
██║░░██╗██║░░██║██║╚████║░░░██║░░░██╔══██║░░░██║░░░██║░░██║░╚═══██╗
╚█████╔╝╚█████╔╝██║░╚███║░░░██║░░░██║░░██║░░░██║░░░╚█████╔╝██████╔╝
░╚════╝░░╚════╝░╚═╝░░╚══╝░░░╚═╝░░░╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═════╝░
""")


lista_contatos = list()
while True:
    os.system("cls")
    titulo()
    print("0 - Sair")
    print("1 - Adicionar contato")
    print("2 - Remover contato")
    print("3 - Listar todos os contatos")
    print("4 - Buscar contatos")
    try:
        option = int(input("Escolha: "))
        if option == 1:
            adicionar_contatos(lista_contatos)

        elif option == 2:
            remover_contato(lista_contatos)

        elif option == 3:
            listar_contato(lista_contatos)
            perguntar_e_limpar()

        elif option == 4:
            buscar_contato(lista_contatos)
        elif option == 0:
            print("Saindo")
            break
    except ValueError:
        print("Digite apenas numeros!")
        perguntar_e_limpar()
