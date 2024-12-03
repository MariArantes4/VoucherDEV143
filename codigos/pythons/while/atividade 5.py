populacaoA = int(input("Informe o valor da primeira população: "))
populacaoB = int(input("Informe o valor da segunda população: "))
taxaA = float(input("Informe a população da primeira taxa: "))
taxaB = float(input("Informe a população da segunda taxa: "))
quantAnos = 0

if populacaoA < populacaoB:
    while populacaoA < populacaoB:
        quantAnos += 1
        populacaoA *= taxaA / 100 + 1
        populacaoB *= taxaB / 100 + 1

else:
    while populacaoA > populacaoB:
        quantAnos += 1
        populacaoA *= taxaA / 100 + 1
        populacaoB *= taxaB / 100 + 1


print(f"{quantAnos} anos")