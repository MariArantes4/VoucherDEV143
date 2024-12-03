def palindromo(palavra):
    palavra = palavra.replace(" ", "")
    
    return palavra == palavra[::-1]

while True:
    palavra = input("Digite uma palavra: ")

    if palindromo(palavra):
        print(f"'{palavra}' é um palíndromo.")
    else:
        print(f"'{palavra}' não é um palíndromo.")
