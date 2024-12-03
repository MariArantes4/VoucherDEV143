salario_atual = float(input("digite seu salario atual:"))

if salario_atual < 500:
    novo_salario= salario_atual* 0.15
elif salario_atual<= 1000:
    novo_salario= salario_atual * 0.10
else:
    novo_salario= salario_atual* 0.05
print("seu salario reajustado é equivalente a: ", novo_salario)