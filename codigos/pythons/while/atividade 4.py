populacaoA = 80000
populacaoB = 200000
quantAnos = 0

while populacaoA < populacaoB:
    quantAnos += 1
    populacaoA *= 1.03
    populacaoB *= 1.015
    

print(f"{quantAnos} anos")