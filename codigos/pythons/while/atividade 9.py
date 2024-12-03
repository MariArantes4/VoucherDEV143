candidato1 = 0
candidato2 = 0
candidato3 = 0
candidato4 = 0
votosNulos = 0
votosBrancos = 0

while  True:
    print(30 * "--")
    print("---OPÇÕES PARA VOTO---")
    print("- Candidato 1 (1)")
    print("- Candidato 2 (2)")
    print("- Candidato 3 (3)")
    print("- Candidato 4 (4)")
    print("- Voto nulo (5)")
    print("- Voto branco (6)")
    print("- Parar encerrar a votação (0)")
    print(30 * "--")

    voto = int(input("Insira aqui o código para seu respectivo voto: "))
    print(" ")

    if voto == 0:
        break
    elif voto == 1:
        candidato1 = candidato1 + 1
        #ou candidato1 += 1
    elif voto == 2:
        candidato2 = candidato2 + 1
    elif voto == 3:
        candidato3 = candidato3 + 1
    elif voto == 4:
        candidato4 = candidato4 + 1
    elif voto == 5:
        votosNulos = votosNulos + 1
    elif voto == 6:
        votosBrancos = votosBrancos + 1
    elif voto not in [1,2,3,4,5,6,0]:
        print("Código de opção de voto inválido. Por favor, tente novamente.")
        continue

print(f"Votos para candidato 1: {candidato1}")
print(f"Votos para candidato 2: {candidato2}")
print(f"Votos para candidato 3: {candidato3}")
print(f"Votos para candidato 4: {candidato4}")
print(f"Votos nulos: {votosNulos}")
print(f"Votos em branco: {votosBrancos}")