numeros = []

for i in range(5):
    numero = int(input("Digite um número: "))
    numeros.append(numero)

maior_numero = numeros[0]

for numero in numeros:
    if numero > maior_numero:
        maior_numero = numero

print("O maior número é:", maior_numero)
