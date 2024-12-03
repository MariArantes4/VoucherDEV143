contador = 0 
numero = int(input("digite um numero")) 
while True:
    
    numero -= 1
    contador +=1

    if numero == 0:
        break

    print("Contador:", contador)