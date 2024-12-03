dicionario_notas = {}

dicionario_notas["Nota 1"] = float(input("Insira a primeira nota: "))
dicionario_notas["Nota 2"] = float(input("Insira a segunda nota: "))
dicionario_notas["Nota 3"] = float(input("Insira a terceira nota: "))
dicionario_notas["Nota 4"] = float(input("Insira a quarta nota: "))

media_notas = (dicionario_notas["Nota 1"] + dicionario_notas["Nota 2"] + dicionario_notas["Nota 3"] + dicionario_notas["Nota 4"]) / 4

print("")
print("---NOTAS E SUAS  MÉDIAS---")
print("")
print(dicionario_notas)
print(f"Essa é a média das notas: {media_notas}")