l = 0

def mostrar_menu():
    print("\nMENU")
    print("1 - Adicionar Tarefa")
    print("2 - Lista de Tarefas")
    print("3 - Marcar como Concluida")
    print("4 - Remover Tarefa")
    print("5 - Sair")

def adicionar_tarefa(tarefas):
    descrição = input("Digite a tarefa que será adicionada: ")
    tarefa = {"descrição": descrição, "status": "não concluida"}
    tarefas.append(tarefa)
    print("tarefa adicionada com sucesso")

def lista_tarefa(tarefas):
    if not tarefas:
        print("nenhuma tarefa a ser exibida")
        return
    
    print(" ")
    print("LISTA DE TAREFAS")

    for i, tarefas in enumerate(tarefas, 1):
        status = tarefas["status"]
        descriçao = tarefas["descrição"]
        print(f"{i}- {descriçao} -- {status}")

def concluidas(tarefas):
    lista_tarefa(tarefas)   
    if not tarefas:
        return
    
    print("")
    n = int(input("Insira o número da tarefa que você quer que seja marcada como concluída: "))
    
    if 1 <= n <= len(tarefas):
        tarefas[n - 1]["status"] = "Concluída"
        print("")
        print("TAREFA MARCADA COMO CONCLUÍDA.")
    
    else:
        print("")
        print("OPÇÃO NÃO VÁLIDA.")

def removerTarefa(tarefas):
    lista_tarefa(tarefas)
    
    if not tarefas:
        return
    
    print("")
    numero = int(input("Digite o número da tarefa a ser removida: "))
    
    if 1 <= numero <= len(tarefas):
        tarefas.pop(numero - 1)
        print("")
        print("TAREFA REMOVIDA DA LISTA DE TAREFAS.")
    
    else:
        print("")
        print("OPÇÃO NÃO VÁLIDA.")

def Opções():
    tarefas = []
    
    while True:
        mostrar_menu()
        print("")
        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            adicionar_tarefa(tarefas)
        elif opcao == 2:
            lista_tarefa(tarefas)
        elif opcao == 3:
            concluidas(tarefas)
        elif opcao == 4:
            removerTarefa(tarefas)
        elif opcao == 0:
            print("")
            print("Saindo do sistema...")
            break
        
        else:
            print("")
            print("OPÇÃO NÃO VÁLIDA. TENTE NOVAMENTE.")

if l == 0:
    Opções()