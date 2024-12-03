funcionarios = []
maior = 0

for i in range(4):

    dados = {}
    dados["nome"] = input("digite um nome: ")
    dados["funçao"] = input("digite sua função: ")
    dados["salario"] = float(input("digite seu salario: "))
      
    funcionarios.append(dados)

    if dados["salario"] > maior:
        maior = dados["salario"]

    for pessoa in funcionarios:
        if pessoa["salario"] == maior:
            print (f"pessoa com maior salario é {pessoa["nome"]}")