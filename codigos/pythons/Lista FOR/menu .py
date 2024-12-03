produtos = ["camisa", "calça", "moletom", "tênis"]
carrinho = [ ]

while True:
    print("1 - Lista de produtos")
    print("2 - Visualizar o carrinho")
    print("3 - Sair")
    opção = int(input("Digite a opção desejada do menu: "))

    if opção == 3:
        print("fechando o menu...")
        break
    elif opção == 2:
        print (f"Produtos = {carrinho}")
    elif opção == 1:
        print("1 - camisa")
        print("2 - calça")
        print("3 - moletom")
        print("4 - tênis")
        codproduto = int(input("Digite o código do produto que deseja adicionar ao carrinho: "))

        if codproduto == 1:
            carrinho.append("camisa")
        elif codproduto == 2:
            carrinho.append("calça")
        elif codproduto == 3:
            carrinho.append("moletom")
        elif codproduto == 4:
            carrinho.append("tênis")