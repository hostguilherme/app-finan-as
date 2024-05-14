from models.usuario import Usuario
from templates.menu import menu
def main():
    
    while True:

        print("\n1. Cadastrar Novo Usuário")
        print("2. Fazer Login")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            Usuario.cadastrar()
        elif opcao == '2':
            dados_usuario = Usuario.fazer_login()
            menu(dados_usuario)
        elif opcao == '3':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Por favor, escolha novamente.")

if __name__ == "__main__":
    main()
