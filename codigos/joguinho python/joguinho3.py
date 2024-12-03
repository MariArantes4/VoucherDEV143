sala_rio= float(input("Digite o salario:"))
prestação= float(input("digite o valor da prestação:"))

prestaçao_limite= sala_rio*0.2

if prestação> prestaçao_limite:
    print("emprestimo concedido")
else:
    print("emprestimo não concedido")