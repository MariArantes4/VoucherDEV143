preco_etiqueta = float(input("Digite o preço do produto: "))
condicao_pagamento = int(input("Digite o código da condição de pagamento (1, 2, 3 ou 4): "))

if condicao_pagamento == 1:
    preco_final = preco_etiqueta * 0.9  
elif condicao_pagamento == 2:
    preco_final = preco_etiqueta * 0.95  
elif condicao_pagamento == 3:
    preco_final = preco_etiqueta  
elif condicao_pagamento == 4:
    preco_final = preco_etiqueta * 1.1
else:
    print("Código de condição de pagamento inválido.")
    exit()

print(f"O valor a ser pago é R$ {preco_final:.2f}")
