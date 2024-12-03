salario_inicial = 1000

salario_atual = salario_inicial + (salario_inicial * 0.015)

ano = 1997
porcentual_aumento = 0.015*2

while ano <= 2024:
    print(f"{salario_atual} = {salario_atual} + ({salario_atual} * {porcentual_aumento}")
    salario_atual = salario_atual + (salario_atual * porcentual_aumento)
    porcentual_aumento = porcentual_aumento * 2
    ano = ano + 1

    print (f"{ano} = {salario_atual}")