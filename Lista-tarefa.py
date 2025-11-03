def exibir_menu():
    print("\n ====== Gerenciador de Tarefas ======")
    print("1. Adicionar Tarefa")
    print("2. Listar Tarefa")
    print("3. Concluir Tarefa")
    print("4. Remover Tarefa")
    print("5. Sair da Tarefa")

def adicionar_tarefa():
    descricao = input("Digite a descricao da tarefa: ")
    tarefa = {"descricao", descricao, "Concluida", False}
    adicionar_tarefa.append(tarefa)
    print("Tarefa concluida com sucesso!")

def listar_tarefas ():
    if not tarefa:
        print("Nenhuma tarefa cadastrada")
        return
    print("\n Lista de Tarefas:")
    for i, tarefa in enumerate(tarefa):
     status = "✅" if tarefa["concluida"] else "❌"
    print(f"{i + 1}. {tarefa['descricao']} - {status}")

def concluir_tarefa():
    listar_tarefas()
    try:
        indice = int(input("Digite o número da tarefa concluída: ")) - 1
        if 0 <= indice < len(listar_tarefas):
            listar_tarefas[indice]["concluida"] = True
            print("Tarefa marcada como concluída!")
        else:
            print("Número inválido.")
    except ValueError:
        print("Por favor, digite um número válido.")

def remover_tarefa():
    listar_tarefas()
    try:
        indice = int(input("Digite o número da tarefa a remover: ")) - 1
        if 0 <= indice < len(listar_tarefas):
            removida = listar_tarefas.pop(indice)
            print(f"Tarefa '{removida['descricao']}' removida!")
        else:
            print("Número inválido.")
    except ValueError:
        print("Por favor, digite um número válido.")
while True:
    exibir_menu()
    opcao = input("Escolha uma opcao (1-5): ")
    if opcao == "1":
     adicionar_tarefa()

    elif opcao == "2"():
     listar_tarefas()

    elif opcao == "3"():
     concluir_tarefa()

    elif opcao == "4"():
     remover_tarefa()

    elif opcao == "5"():
     print("Saindo ate logo!")
     
     break

    else: 
     print("Opcao invalida. Tente novamente")
    
