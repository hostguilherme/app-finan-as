from models.despesa import Despesa

def main_despesa(user_id):
    while True:
        print("Bem-vindo ao seu sistema de gerenciamento:")

        print("1. Adicionar Despesa")
        print("2. Remover Despesa")
        print("3. Visualizar Despesas")
        print("4. Sair")

        escolha = input("Escolha a opção: ")

        if escolha == '1':
            adicionar_despesa(user_id)
            print("Despesa adicionada com sucesso!")
        elif escolha == '2':
            remover_despesa(user_id)
        elif escolha == '3':
            visualizar_despesas(user_id)
        elif escolha == '4':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Por favor, escolha novamente.")

def adicionar_despesa(user_id):
    categoria = input("Digite a categoria da despesa: ")
    valor = float(input("Digite o valor da despesa: "))
    descricao = input("Digite a descrição da despesa: ")
    data = input("Digite a data da despesa (no formato YYYY-MM-DD): ")
    hora = input("Digite a hora da despesa (no formato HH:MM): ")
    Despesa.adicionar_despesa(user_id, categoria, valor, descricao, data, hora)

def remover_despesa(user_id):
    despesas = Despesa.visualizar_despesas(user_id)
    if despesas:
        print("Lista de despesas:")
        for idx, despesa in enumerate(despesas, start=1):
            print(f"{idx}. {despesa}")
        opcao = int(input("Escolha o número da despesa que deseja remover: "))
        if 1 <= opcao <= len(despesas):
            despesa_id = despesas[opcao - 1][0]  # Pega o ID da despesa selecionada
            Despesa.remover_despesa(despesa_id)
            print("Despesa removida com sucesso!")
        else:
            print("Opção inválida.")
    else:
        print("Nenhuma despesa encontrada.")

def visualizar_despesas(user_id):
    despesas = Despesa.visualizar_despesas(user_id)
    if despesas:
        print("Lista de despesas:")
        for despesa in despesas:
            print(despesa)
    else:
        print("Nenhuma despesa encontrada.")
