caderno = 3
caneta = 68
lapis = 87
borracha = 6
regua = 14

while True:

    print(30 * ("--"))
    print("---OPERAÇÕES---")
    print(" E - Entrada de estoque")
    print(" S - Saída de estoque")
    print(" R - Relatório")
    print(" X - Sair")
    print(30 * "--")

    operacao = input("Escolha a operação que deseja fazer: ")
    
    if operacao == "E" and "e":
        print(30 * "--")
        print("- Caderno (10)")
        print("- Caneta (20)")
        print("- Lápis (30)")
        print("- Borracha (40)")
        print("- Régua (50)")
        print(30 * ("--"))
        codigo_entrada = int(input("Digite o número o código do produto que irá entrar no estoque: "))
        quant_entrada = int(input("Insira a quantidade que entrara no estoque: "))

        if codigo_entrada == 10:
            caderno = caderno + quant_entrada
        elif codigo_entrada == 20:
            caneta = caneta + quant_entrada
        elif codigo_entrada == 30:
            lapis = lapis + quant_entrada
        elif codigo_entrada == 40:
            borracha = borracha + quant_entrada
        elif codigo_entrada == 50:
            regua = regua + quant_entrada

    elif operacao == "S":
        print(30 * "--")
        print("- Caderno (10)")
        print("- Caneta (20)")
        print("- Lápis (30)")
        print("- Borracha (40)")
        print("- Régua (50)")
        print(30 * ("--"))
        codigo_saida = int(input("Digite o número o código do produto que irá sair do estoque: "))
        quant_saida = int(input("Insira a quantidade que sairá do estoque: "))

        if codigo_saida == 10:
            if caderno < quant_saida:
                print("A quantidade inserida é maior do que a quantia em estoque.")
            else:
                caderno = caderno - quant_saida
        elif codigo_saida == 20:
            if caneta < quant_saida:
                print("A quantidade inserida é maior do que a quantia em estoque.")
            else:
                caneta = caneta - quant_saida
        elif codigo_saida == 30:
            if lapis < quant_saida:
                print("A quantidade inserida é maior do que a quantia em estoque.")
            else:
                lapis = lapis - quant_saida
        elif codigo_saida == 40:
            if borracha < quant_saida:
                print("A quantidade inserida é maior do que a quantia em estoque.")
            else:
                borracha = borracha - quant_saida
        elif codigo_saida == 50:
            if regua < quant_saida:
                print("A quantidade inserida é maior do que a quantia em estoque.")
            else:
                regua = regua - quant_saida
    
    elif operacao == "R":
        print(f"Quantia de cadernos: {caderno}")
        print(f"Quantia de cenetas: {caneta}")
        print(f"Quantia de lapís: {lapis}")
        print(f"Quantia de borrachas: {borracha}")
        print(f"Quantia de réguas: {regua}")

    elif operacao == "X":
        print("Encerrando o estoque...")
        break