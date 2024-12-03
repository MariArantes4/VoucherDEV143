while True:
    nota = float(input("Digite uma nota entre 0 e 10: "))
    if 0 <= nota <= 10:
        print(f"Você digitou a nota {nota}.")
        break
    else:
        print("Valor inválido. A nota deve estar entre 0 e 10.")
