numero = input("digite um numero:")
soma= 0
while True:
    while numero != "":
        if numero> 0:
            soma = soma + int(numero[0]) 
            numero = numero[1:]

        elif numero == 0:
            print(soma)
            break
        else:
            print("invalido")