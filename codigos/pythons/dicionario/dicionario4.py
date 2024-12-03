lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

soma_pares = 0
soma_impares = 0

def verificar_par_ou_impar(numero):
    if numero % 2 == 0:
        return "par"
    else:
        return "impar"

for numero in lista_numeros:
    if verificar_par_ou_impar(numero) == "par":
        soma_pares += numero
    else:
        soma_impares += numero

print("Soma dos números pares:", soma_pares)
print("Soma dos números ímpares:", soma_impares)
