class Carro:
    motor_ligado = False
    carro_andando = False

    cor = "sem cor"
    marca = "sem marca"
    modelo = "sem modelo"
    ano = 0
    km_rodados = 0

    def LigarMotor():
        
        if not Carro.motor_ligado:
            Carro.motor_ligado = True
            print("")
            print("O MOTOR ESTÁ LIGADO")
            print("")
        else:
            print("")
            print("O MOTOR DO CARRO JÁ ESTÁ DESLIGADO")
            print("")

    def DesligarMotor():
        if Carro.motor_ligado:
            if not Carro.carro_andando:
                Carro.motor_ligado = False
                print("")
                print("O MOTOR DO CARRO JÁ ESTÁ DESLIGADO")
                print("")
            else:
                print("")
                print("NÃO É POSSÍVEL DESLIGAR O MOTOR ENQUANTO O CARRO ESTÁ ANDANDO")
                print("")
        else:
            print("")
            print("O MOTOR DO CARRO JÁ ESTÁ DESLIGADO")
            print("")

    def Andar():
        if Carro.motor_ligado:
            if not Carro.carro_andando:
                Carro.carro_andando = True
                print("")
                print("CARRO ANDANDO")
                print("")
            else:
                print("")
                print("O CARRO JÁ ESTÁ ANDANDO")
                print("")
        else:
            print("")
            print("NÃO É POSSÍVEL ANDAR COM O CARRO DESLIGADO")
            print("")

    def Parar():
        if Carro.carro_andando:
            Carro.carro_andando = False
            print("")
            print("CARRO PARADO")
            print("")
        else:
            print("")
            print("O CARRO JÁ ESTÁ PARADO")
            print("")

    def StatusMotor():
        status = "LIGADO" if Carro.motor_ligado else "DESLIGADO"
        print("")
        print(f"O MOTOR ESTÁ {status}")
        print("")

    def StatusCarro():
        status = "ANDANDO" if Carro.carro_andando else "PARADO"
        print("")
        print(f"O CARRO ESTÁ {status}")
        print("")
    
    def detalhes(self):
        print("")
        print(f"- Cor: {self.cor}")
        print(f"- Marca: {self.marca}")
        print(f"- Modelo: {self.modelo}")
        print(f"- Ano: {self.ano}")
        print(f"- KMs rodados: {self.km_rodados}")
        print("")

carro1 = Carro()
carro1.cor = "Azul"
carro1.marca = "Audi"
carro1.modelo = "RS5"
carro1.ano = 2023
carro1.km_rodados = 0


def Menu():
    while True:
        print(30 * "--")
        print("---MENU---")
        print("1 - Ligar motor")
        print("2 - Desligar motor")
        print("3 - Fazer o carro andar")
        print("4 - Parar os carros")
        print("5 - Ver status do motor")
        print("6 - Ver status do carro")
        print("7 - Ver detalhe do carro")
        print("0 - Sair")
        print("")

        op = int(input("Insira o número da sua opção: "))
        print(30 * "--")

        if op == 1:
            Carro.LigarMotor()
        elif op == 2:
            Carro.DesligarMotor()
        elif op == 3:
            Carro.Andar()
        elif op == 4:
            Carro.Parar()
        elif op == 5:
            Carro.StatusMotor()
        elif op == 6:
            Carro.StatusCarro()
        elif op == 7:
            carro1.detalhes()
        elif op == 0:
            print("")
            print("Bye Bye...")
            print("")
            break
        else:
            print("")
            print("Opção inválida. Tente novamente.")
            print("")

Menu()