codigo_mais_alto = codigo_mais_baixo = codigo_mais_gordo = codigo_mais_magro = None
altura_mais_alto = altura_mais_baixo = peso_mais_gordo = peso_mais_magro = 0
total_alturas = total_pesos = num_clientes = 0

while True:
    codigo = input("Digite o código do cliente (ou 0 para encerrar): ")
    if codigo == '0':
        break
    
    altura = float(input("Digite a altura do cliente em metros: "))
    peso = float(input("Digite o peso do cliente em quilogramas: "))
    
    if altura > altura_mais_alto:
        codigo_mais_alto, altura_mais_alto = codigo, altura
    if altura < altura_mais_baixo or altura_mais_baixo == 0:
        codigo_mais_baixo, altura_mais_baixo = codigo, altura
    if peso > peso_mais_gordo:
        codigo_mais_gordo, peso_mais_gordo = codigo, peso
    if peso < peso_mais_magro or peso_mais_magro == 0:
        codigo_mais_magro, peso_mais_magro = codigo, peso
    
    total_alturas += altura
    total_pesos += peso
    num_clientes += 1

media_alturas = total_alturas / num_clientes if num_clientes > 0 else 0
media_pesos = total_pesos / num_clientes if num_clientes > 0 else 0

print("\nCliente mais alto:")
print(f"Código: {codigo_mais_alto}, Altura: {altura_mais_alto:.2f}m")
print("\nCliente mais baixo:")
print(f"Código: {codigo_mais_baixo}, Altura: {altura_mais_baixo:.2f}m")
print("\nCliente mais gordo:")
print(f"Código: {codigo_mais_gordo}, Peso: {peso_mais_gordo:.2f}kg")
print("\nCliente mais magro:")
print(f"Código: {codigo_mais_magro}, Peso: {peso_mais_magro:.2f}kg")
print("\nMédia das alturas dos clientes:", media_alturas)
print("Média dos pesos dos clientes:", media_pesos)
