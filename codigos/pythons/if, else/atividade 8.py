primero_produto = float(input("Insira o valor do primeiro produto: "))
segundo_produto = float(input("Insira o valor do segundo produto: "))
terceiro_produto  = float(input("Innsira o valor do terceiro produto: "))

if primero_produto < segundo_produto and primero_produto < terceiro_produto:
    print("Compre o primeiro produto.")

if segundo_produto < primero_produto and segundo_produto < terceiro_produto:
    print("Compre o segundo produto.")

if terceiro_produto < primero_produto and terceiro_produto < segundo_produto:
    print("Compre o  terceiro produto.")
