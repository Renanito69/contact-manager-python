import os

def adicionar_contatos(lista_contatos):
    os.system('cls')
    print("Adicinando contato")
    contato = dict()
    contato['nome'] = str(input("Nome: "))
    contato['telefone'] = int(input("Numero: "))
    return lista_contatos.append(contato)

def listar_contato(lista_Contatos):
    for contato in lista_Contatos:
        print(f"{contato['nome']} -> {contato['telefone']}")
    perguntar_e_limpar()


def perguntar_e_limpar():
    input("\nDigite uma tecla para voltar para o menu: ")
    os.system("cls")
    
    
def remover_contato(lista_Contatos):
    pass

def buscar_contato(lista_Contatos):
    pass
    
lista_contatos = list()
while True:
    os.system("cls")
    print("0 - Sair")
    print("1 - Adicionar contato")
    print("2 - Remover contato")
    print("3 - Listar todos os contatos")
    print("4 - Buscar contatos")

    option = int(input("Escolha: "))

    if option == 1:
        adicionar_contatos(lista_contatos)

    elif option == 2:
        pass
    
    elif option == 3:
        listar_contato(lista_contatos)
    
    elif option == 4:
        pass
    elif option == 0:
        print("Saindo")
        break