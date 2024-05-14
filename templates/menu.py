from models.usuario import Usuario
from models.renda import Renda
def menu(dados_usuario):
    user = dados_usuario[1]
    id = dados_usuario[0]
    while True:

        print(f"Bem vindo ao seu sistema de gerenciamento:{user} ")

        print("1. Adicionar Renda")

        print("2. Despesa")

        print("3. Extrato")

        print("4. Estatisticas")

        print("5. Poupança")

        print("6. Configurações do Usuário")

        print("7. Sair")

        escolha = input("Escolha a opção: ")

        if escolha == '1': 
            Renda.adicionar_renda(id)

        elif escolha == '2':

            pass

        elif escolha == '3':

            pass

        elif escolha == '4':
            pass
            
        elif escolha == '5':
            pass

        elif escolha == '6':
           pass
        
        elif escolha == '7':
            pass

        else:
            print("Opção inválida. Tente novamente.")


