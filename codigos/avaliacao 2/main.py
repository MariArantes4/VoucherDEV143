from barbearia import Barbearia
from agendamento import Cliente

def ExibirMenu():
    print(" ")
    print("--------------MENU--------------")
    print("1- AGENDAR")
    print("2- CANCELAR AGENDAMENTO")
    print("3- VISUALIZAR AGENDAMENTOS")
    print("0- SAIR")
    print(" ")

ExibirMenu()

barbearia = Barbearia()
while True:
    try:
        op = int(input("Digite a opção desejada: "))
        if op == 1:
            nome = input("Digite seu nome: ")
            try:
                data = float(input("Digite a data que deseja ser atendido (formato DD/MM/AAAA): "))
                hora = float(input("Digite a hora que deseja ser atendido (formato HH.MM): "))
            except ValueError:
                print("Formato de data ou hora inválido. Tente novamente.")
                
            servico = input("Digite o serviço que deseja: ")
            cliente = Cliente(nome, data, hora, servico)
            barbearia.AgendarCliente(cliente)
            print("Seu agendamento realizado com sucesso!")

   
        elif op == 2:
            cliente = input("Digite seu nome: ")
            if barbearia.CancelarAgendamento(nome):
                print("Agendamento cancelado com sucesso!")
            else:
                print("Nenhum agendamento encontrado para esse nome")

        if op == 3:
            agendamento = input("Digite seu nome: ")
            detalhes = barbearia.BuscarAgendamento(nome)
            if detalhes:
                print(detalhes)
            else:
                print("Nenhum agendamento encontrado para esse nome.")
        
        if op == 0:
            print("Bye Bye...")
            break
    except ValueError:
        print("Opção inválida. Por favor, insira um número.")

        