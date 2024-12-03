while True:
    print("Calculadora:")
    print("1 - Multiplicação")
    print("2 - Divisão")
    print("3 - Adição")
    print("4 - Subtração")
    print("5 - Sair")

    opcao = input("Escolha uma operação (1/2/3/4/5): ")

    if opcao == "5":
        print("bye bye calculadora...")
        break

    if opcao not in ["1", "2", "3", "4"]:
        print("Opção inválida. Por favor, escolha uma opção válida.") 
        continue

    valor1 = float(input("Digite o primeiro valor: "))
    valor2 = float(input("Digite o segundo valor: "))

    if opcao == "1":
        resultado = valor1 * valor2
        print("O resultado da multiplicação é:", {resultado})
    elif opcao == "2":
        if valor2 != 0:
            resultado = valor1 / valor2
            print("O resultado da divisão é:", {resultado})
        else:
            print("Não é possível dividir por zero.")
    elif opcao == "3":
        resultado = valor1 + valor2
        print("O resultado da adição é:", {resultado})
    elif opcao == "4":
        resultado = valor1 - valor2
        print("O resultado da subtração é:", {resultado})
