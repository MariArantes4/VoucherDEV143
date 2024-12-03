pacientes = {}
consultas = []

while True:
    print("1. Entrar como Usuário")
    print("2. Entrar como Médico")
    print("3. Sair")
    opcao = int(input("Selecione a opção desejada: "))

    if opcao == 1:
        while True:
            print("1. Marcar Consulta")
            print("2. Ver Histórico de Consultas")
            print("3. Voltar")
            opcao_usuario = int(input("Selecione a opção desejada: "))

            if opcao_usuario == 1:
                nome = input("Nome do Paciente: ")
                cpf = input("CPF: ")
                idade = input("Idade: ")
                horario = input("Horário da Consulta: ")

                nova_consulta = {"nome": nome, "cpf": cpf, "idade": idade, "horario": horario}
                consultas.append(nova_consulta)

                if cpf not in pacientes:
                    pacientes[cpf] = {"nome": nome, "idade": idade}

                print("Consulta marcada com sucesso!")
            elif opcao_usuario == 2:
                cpf = input("Digite o CPF para ver o histórico: ")
                print("Histórico de Consultas:")
                for consulta in consultas:
                    if consulta["cpf"] == cpf:
                        print(f"Nome: {consulta['nome']}, Horário: {consulta['horario']}")
            elif opcao_usuario == 3:
                break
            else:
                print("Opção inválida!")

    elif opcao == 2:
        while True:
            print("1. Ver Lista de Pacientes")
            print("2. Realizar Consulta")
            print("3. Voltar")
            opcao_medico = int(input("Selecione a opção desejada: "))

            if opcao_medico == 1:
                print("Lista de Pacientes com Consulta:")
                for consulta in consultas:
                    print(f"Nome: {consulta['nome']}, CPF: {consulta['cpf']}, Horário: {consulta['horario']}")
            elif opcao_medico == 2:
                cpf = input("CPF do Paciente a ser atendido: ")
                for consulta in consultas:
                    if consulta["cpf"] == cpf:
                        consultas.remove(consulta)
                        print("Consulta realizada e paciente liberado!")
                        break
            elif opcao_medico == 3:
                break
            else:
                print("Opção inválida!")

    elif opcao == 3:
        break
    else:
        print("Opção inválida!")
