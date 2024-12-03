preco_file_duplo_ate_5kg = 34.90
preco_file_duplo_acima_5kg = 35.80
preco_alcatra_ate_5kg = 44.90
preco_alcatra_acima_5kg = 46.80
preco_picanha_ate_5kg = 66.90
preco_picanha_acima_5kg = 67.80

tipo_carne = input("Digite o tipo de carne desejado (File Duplo, Alcatra ou Picanha): ").lower()
quantidade = float(input("Digite a quantidade em Kg desejada: "))

if tipo_carne == "file duplo":
    if quantidade <= 5:
        preco_total = quantidade * preco_file_duplo_ate_5kg
    else:
        preco_total = quantidade * preco_file_duplo_acima_5kg
elif tipo_carne == "alcatra":
    if quantidade <= 5:
        preco_total = quantidade * preco_alcatra_ate_5kg
    else:
        preco_total = quantidade * preco_alcatra_acima_5kg
elif tipo_carne == "picanha":
    if quantidade <= 5:
        preco_total = quantidade * preco_picanha_ate_5kg
    else:
        preco_total = quantidade * preco_picanha_acima_5kg
else:
    print("Tipo de carne inválido.")
    exit()

pagamento = input("Digite o tipo de pagamento (Cartão Tabajara ou outro): ").lower()
if pagamento == "cartão tabajara":
    desconto = preco_total * 0.05
else:
    desconto = 0

valor_a_pagar = preco_total - desconto

print("\nCUPOM FISCAL")
print(f"Tipo de carne: {tipo_carne.capitalize()}")
print(f"Quantidade: {quantidade:.2f} Kg")
print(f"Preço total: R$ {preco_total:.2f}")
print(f"Tipo de pagamento: {pagamento.capitalize()}")
print(f"Desconto: R$ {desconto:.2f}")
print(f"Valor a pagar: R$ {valor_a_pagar:.2f}")