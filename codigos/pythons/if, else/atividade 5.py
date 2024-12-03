def calcular_raizes(a, b, c):
    if a == 0:
        print("Esta não é uma equação do 2º grau.")
        return
    delta = b**2 - 4*a*c

    if delta < 0:
        print("A equação não possui raízes reais.")
    elif delta == 0:
        raiz = -b / (2*a)
        print(f"A equação possui uma raiz real: ", raiz)
    else:
        raiz1 = (-b + delta**0.5) / (2*a)
        raiz2 = (-b - delta**0.5) / (2*a)
        print(f"A equação possui duas raízes reais: {raiz1} e {raiz2}")

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))
    
calcular_raizes(a, b, c)
