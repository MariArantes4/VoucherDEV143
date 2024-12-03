def exibir_menu():
    print("\nMenu:")
    print("1. Adicionar tarefa")
    print("2. Listar tarefas")
    print("3. Marcar tarefa como concluída")
    print("4. Remover tarefa")
    print("5. Sair")

def adicionar_tarefa(tarefas):
    descricao = input("Digite a descrição da tarefa: ")
    tarefa = {"descricao": descricao, "status": "Não Concluída"}
    tarefas.append(tarefa)
    print("Tarefa adicionada com sucesso!")

def listar_tarefas(tarefas):
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return

    print("\nLista de Tarefas:")
    for i, tarefa in enumerate(tarefas, 1):
        status = tarefa["status"]
        descricao = tarefa["descricao"]
        print(f"{i}. {descricao} - {status}")

def marcar_como_concluida(tarefas):
    listar_tarefas(tarefas)
    if not tarefas:
        return

    numero = int(input("Digite o número da tarefa a ser marcada como concluída: "))
    if 1 <= numero <= len(tarefas):
        tarefas[numero - 1]["status"] = "Concluída"
        print("Tarefa marcada como concluída!")
    else:
        print("Número inválido.")

def remover_tarefa(tarefas):
    listar_tarefas(tarefas)
    if not tarefas:
        return

    numero = int(input("Digite o número da tarefa a ser removida: "))
    if 1 <= numero <= len(tarefas):
        tarefas.pop(numero - 1)
        print("Tarefa removida com sucesso!")
    else:
        print("Número inválido.")

def main():
    tarefas = []
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_tarefa(tarefas)
        elif opcao == "2":
            listar_tarefas(tarefas)
        elif opcao == "3":
            marcar_como_concluida(tarefas)
        elif opcao == "4":
            remover_tarefa(tarefas)
        elif opcao == "5":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
