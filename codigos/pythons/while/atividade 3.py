while True:
    nome = input("Inisra seu nome (deve conter mais de 3 caracteres): ")
    
    if nome == nome[0:2]:
        print("Nome inválido. Tente novamente.")
        continue
    else:
        print("Nome válido.")

    idade = int(input("Insira sua idade (entre 0 e 150 anos): "))

    if idade < 0 or idade > 150:
        print("Idade inválida. Tente Novamente.")
        continue
    else:
        print("Idade válida.")

    salario = float(input("Informe seu salário (deve ser maior que 0 reais): "))

    if salario < 0:
        print("Valor do salário é inválido. Tente novamente.")
        continue
    else:
        print("Valor do salário é válido.")
        
    sexo = input("Informe seu sexo f(feminino), m(masculino) ou o(outro): ")

    if sexo not in ["f","m","o"]:
        print("Sexo inválido. Tente novamente.")
        continue
    else:
        print("Sexo válido.")

    estadocivil = input("Informe seu estado civil (s(solteiro), c(casado), v(viúvo) ou d(divorciado)): ")

    if estadocivil not in ["s","c","v","d"]:
        print("Estado civil inváido. Tente novamente.")
    else:
        print("Estado civil válido.")
        print("CADASTRO VÁLIDO.")
        break