n = input("Digite um numero menor que 1000")

if(int(n) > 1000):
    print("Numero invalido")
else:
    if(int(n) >= 100):
        cent = int(n[0])
        deze = int(n[1])
        uni = int(n[2])
        centTexto = "centenas"
        dezeTexto = "Dezenas"
        uniTexto = "Unidades"

        if(cent == 1):
            centTexto = "Centena"
        if(deze == 1):
            dezeTexto = "Dezena"
        if(uni == 1):
            uniTexto = "Unidade"
        
        print(f"{n} = {cent} {centTexto}, {deze} {dezeTexto} e {uni} {uniTexto}")
    elif(int(n) >= 10 and int(n) < 99 ):
        deze = int(n[0])
        uni = int(n[1])
        dezeTexto = "Dezenas"
        uniTexto = "Unidades"
        if(deze == 1):
            dezeTexto = "Dezena"
        if(uni == 1):
            uniTexto = "Unidade"
        
        print(f"{n} = {deze} {dezeTexto} e {uni} {uniTexto}")
    else:
        uni = int(n)
        uniTexto = "Unidades"

        if(uni == 1):
            uniTexto = "Unidade"
        print(f"{n} = {uni} {uniTexto}")