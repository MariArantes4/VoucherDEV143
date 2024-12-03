higiene = [["Sabonete",2.50,100],["Pasta de Dente",3.00,101],["Escova de Dente",2.20,102]]
limpeza = [["Detergente",1.10,200],["Esponja",0.80,201],["Sabão em Pó",9.40,202]]
doces = [["Bicoito/Bolacha Recheado",2.20,300],["Pacote de Bala",12.10,301],["Caixa de Bombom",9.90,302]]
graos = [["Arroz Branco 1kg",13.00,400],["Feijão Preto 1Kg",12.00,401],["Lentilha 1Kg",9.50,402]]
gerais = [["Óleo 1L",6.50,500],["Pão de Forma",4.80,501],["Sal 1kg",1.45,502],["Àçucar 1Kg",4.90,503],["Leite 1L",3.90,504]]
carnes = [["Carne Moída 1Kg",20.70,600],["Filé de Frango 1Kg",18.90,601],["Posta de Tilápia 1Kg",25.90,602]]
bebidas = [["Suco de Laranja 1L",6.60,700],["Refrigerante Coca Cola 2L",9.90,701],["Água Mineral 1L",2.20,702]]
hortifruti = [["Banana Nanica 1Kg",2.90,800],["Batata Inglesa 1Kg",4.40,801],["Alface Americana Uni",1.50,802]]

carrinho = []
total_compra = 0

while True:
    print(30 * "--")
    print("---MERCADO---")
    print(" Selecione seu tipo de usuário: ")
    print("- Funcionário (1)")
    print("- Cliente (2)")
    print("- Sair do Mercado (0)")
    print(" ")
   
    tipo_usuario = int(input("Insira aqui o número do seu tipo de usuário: "))
    print(30 * "--")

    if tipo_usuario == 0:
        print(" ")
        print("Saindo do mercado...")
        break
       
    elif tipo_usuario == 2:
       
        nome_cliente = input("Insira seu nome: ")
        cpf_cliente = input("Insira seu CPF: ")
       
        while True:
            print(30 * "--")
            print("---MERCADINHO---")
            print("- Vizualizar carrinho (1)")
            print("- Olha seções de produtos (2)")
            print("- Remover um produto do carrinho (3)")
            print("- Pagar a compra (4)")
            print("- Sair das Opções (0)")
            print(" ")

            opcao = int(input("Insira aqui o número da operação que deseja realizar: "))
            print(30 * "--")

            if opcao == 0:
                print(" ")
                print("Voltando ao menu de usuário...")
                print(" ")
                break
             
            elif opcao == 1:
                if carrinho:
                    print(" ")
                    print("---CARRINHO---")
                    for i in carrinho:
                        print(f"{i[0]}/Preço: R${i[1]} (Código {i[2]}")
                    print(f"Total da compra: R${total_compra}")
                    print(" ")

                else:
                    print(" ")
                    print("O CARRINHO ESTÁ VAZIO.")
                    print(" ")
               
            elif opcao == 2:
                print(" ")
                print("---LISTA DE PRODUTOS---")
                print(" ")
                print("---PRODUTOS DE HIGIENE---")
                for produto in higiene:
                    print(f"{produto[0]}/Preço: R${produto[1]}/Código: {produto[2]}")
                    print(" ")
                print("---PRODUTOS DE LIMPEZA---")
                for produto in limpeza:
                    print(f"{produto[0]}/Preço: R${produto[1]}/Código: {produto[2]}")
                    print(" ")
                print("---DOCES---")
                for produto in doces:
                    print(f"{produto[0]}/Preço: R${produto[1]}/Código: {produto[2]}")
                    print(" ")
                print("---GRÃOS---")
                for produto in graos:
                    print(f"{produto[0]}/Preço: R${produto[1]}/Código: {produto[2]}")
                    print(" ")
                print("---CARNES---")
                for produto in carnes:
                    print(f"{produto[0]}/Preço: R${produto[1]}/Código: {produto[2]}")
                    print(" ")
                print("---PRODUTOS GERAIS---")
                for produto in gerais:
                    print(f"{produto[0]}/Preço: R${produto[1]}/Código: {produto[2]}")
                    print(" ")
                print("---BEBIDAS---")
                for produto in bebidas:
                    print(f"{produto[0]}/Preço: R${produto[1]}/Código: {produto[2]}")
                    print(" ")
                print("---HORTIFRUTI---")
                for produto in hortifruti:
                    print(f"{produto[0]}/Preço: R${produto[1]}/Código: {produto[2]}")
                    print(" ")
               
                print(30 * "--")
                add_carrinho = int(input("Insira o código do produto que deseja adicionar ao carrinho: "))
                print(" ")
                print(30 * "--")
           
                if add_carrinho >= 100 or add_carrinho <= 199:
                    for i in higiene:
                        produto_adicionado = False
                       
                        if i[2] == add_carrinho:
                            carrinho.append(i)
                            total_compra += i[1]
                            produto_adicionado = True
                            print(f"{i[0]} FOI ADICIONADO AO CARRINHO.")
                            print(" ")
                            print(f"Valor da compra até o momento: R${total_compra}")
                           
                if add_carrinho >= 200 or add_carrinho <= 299:
                    for i in limpeza:
                        produto_adicionado = False
                       
                        if i[2] == add_carrinho:
                            carrinho.append(i)
                            total_compra += i[1]
                            produto_adicionado = True
                            print(f"{i[0]} FOI ADICIONADO AO CARRINHO.")
                            print(" ")
                            print(f"Valor da compra até o momento: R${total_compra}")
               
                if add_carrinho >= 300 or add_carrinho <= 399:
                    for i in doces:
                        produto_adicionado = False
                       
                        if i[2] == add_carrinho:
                            carrinho.append(i)
                            total_compra += i[1]
                            produto_adicionado = True
                            print(f"{i[0]} FOI ADICIONADO AO CARRINHO.")
                            print(" ")
                            print(f"Valor da compra até o momento: R${total_compra}")

                if add_carrinho >= 400 or add_carrinho <= 499:
                    for i in graos:
                        produto_adicionado = False
                       
                        if i[2] == add_carrinho:
                            carrinho.append(i)
                            total_compra += i[1]
                            produto_adicionado = True
                            print(f"{i[0]} FOI ADICIONADO AO CARRINHO.")
                            print(" ")
                            print(f"Valor da compra até o momento: R${total_compra}")

                if add_carrinho >= 500 or add_carrinho <= 599:
                    for i in gerais:
                        produto_adicionado = False
                       
                        if i[2] == add_carrinho:
                            carrinho.append(i)
                            total_compra += i[1]
                            produto_adicionado = True
                            print(f"{i[0]} FOI ADICIONADO AO CARRINHO.")
                            print(" ")
                            print(f"Valor da compra até o momento: R${total_compra}")

                if add_carrinho >= 600 or add_carrinho <= 699:
                    for i in carnes:
                        produto_adicionado = False
                       
                        if i[2] == add_carrinho:
                            carrinho.append(i)
                            total_compra += i[1]
                            produto_adicionado = True
                            print(f"{i[0]} FOI ADICIONADO AO CARRINHO.")
                            print(" ")
                            print(f"Valor da compra até o momento: R${total_compra}")

                if add_carrinho >= 700 or add_carrinho <= 799:
                    for i in bebidas:
                        produto_adicionado = False
                       
                        if i[2] == add_carrinho:
                            carrinho.append(i)
                            total_compra += i[1]
                            produto_adicionado = True
                            print(f"{i[0]} FOI ADICIONADO AO CARRINHO.")
                            print(" ")
                            print(f"Valor da compra até o momento: R${total_compra}")

                if add_carrinho >= 800 or add_carrinho <= 899:
                    for i in hortifruti:
                        produto_adicionado = False
                       
                        if i[2] == add_carrinho:
                            carrinho.append(i)
                            total_compra += i[1]
                            produto_adicionado = True
                            print(f"{i[0]} FOI ADICIONADO AO CARRINHO.")
                            print(" ")
                            print(f"Valor da compra até o momento: R${total_compra}")

            elif opcao == 3:
                if carrinho:
                    print("---CARRINHO---")
                    for i in carrinho:
                        print(f"- {i[0]}: R${i[1]} (Código: {i[2]})")
                        print(" ")
                    remover = int(input("Insira o código do produto que deseja remover do carrinho: "))
                   
                    produto_removido = False
                    for item in carrinho:
                        if item[2] == remover:
                            carrinho.remove(item)
                            total_compra -= item[1]
                            produto_removido = True
                            print(" ")
                            print(f"{item[0]} FOI REMOVIDO DO CARRINHO.")
                            print(" ")
                            print(f"Valor da compra até o momento: R${total_compra}")
                            break
                       
                        elif not produto_removido:
                            print(" ")
                            print("CÓDIGO INVÁLIDO.")
                            print(" ")
                       
                        else:
                            print(" ")
                            print("O CARRINHO ESTÁ VAZIO.")
                            print(" ")
           
            elif opcao ==  4:
               
                while True:
                    print("---ÁREA DE PAGAMENTO---")
                    print(" ")
                    print("- Mostrar produtos do carrinho e finalizar compra (1)")
                    print("- Volta as outras opções do mercado (2)")
                    print(" ")
               
                    finalizar_comprar = int(input("Insira aqui o número da opção escolhida: "))
                    print(30 * "--")
                   
                    if finalizar_comprar == 2:
                        print(" ")
                        print("Voltando para o menu do mercado...")
                        print(" ")
                        break
                   
                    elif finalizar_comprar == 1:
                            if carrinho:
                                print("---CARRINHO---")
                                for i in carrinho:
                                    print(f"- {i[0]}: R${i[1]} (Código: {i[2]})")
                                   
                                    imposto_nacional = total_compra * 0.05
                                    imposto_estadual = total_compra * 0.08
                                    imposto_municipal = total_compra * 0.12
                                    total_impostos = imposto_nacional + imposto_estadual + imposto_municipal
                                    total_com_impostos = total_compra + total_impostos
                               
                                print(30 * "--")
                                print(" ")
                                print(f"Valor da compra: R${total_compra}")
                                print(" ")
                                print(f"Valor do imposto nacional: {imposto_nacional}")
                                print(f"Valor do imposto estadual: {imposto_estadual}")
                                print(f"Valor do imposto municipal: {imposto_municipal}")
                                print(f"Total de Impostos: R${total_impostos}")
                                print(" ")
                                print(f"Total a Pagar: R${total_com_impostos}")
                                print(" ")
                               
                                while True:
                                    print(30 * "--")
                                    print("---INFORME A FORMA DE PAGAMENTO---")
                                    print("- Dinheiro (1)")
                                    print("- Cartão: Débito, Crédito ou Voucher (2)")
                                    print("- Pix (3)")
                                    print(" ")
                                   
                                    forma_pagamento = int(input("Insira aqui o número da opção: "))
                                    print(30 * "--")
                                   
                                    if forma_pagamento == 1:
                                        print(" ")
                                        qt_dinheiro = float(input("Valor que usará para pagamento: "))
                                       
                                        if qt_dinheiro >= total_com_impostos or qt_dinheiro == total_com_impostos:
                                           
                                            troco = qt_dinheiro - total_com_impostos
                                            imposto_nacional = total_compra * 0.05
                                            imposto_estadual = total_compra * 0.08
                                            imposto_municipal = total_compra * 0.12
                                            total_impostos = imposto_nacional + imposto_estadual + imposto_municipal
                                            total_com_impostos = total_compra + total_impostos
                                           
                                            print(30 * "--")
                                            print("---NOTA FISCAL---")
                                            print("-PRODUTOS-")
                                            for i in carrinho:
                                                print(f"- {i[0]}: R${i[1]}")
                                                print(f"Valor total da compra: R${total_compra}")
                                                print(" ")
                                            print(f"Valor do imposto nacional: {imposto_nacional}")
                                            print(f"Valor do imposto estadual: {imposto_estadual}")
                                            print(f"Valor do imposto municipal: {imposto_municipal}")
                                            print(" ")
                                            print(f"Troco: {troco}")
                                            print(f"Total de Impostos: R${total_impostos}")
                                            print(f"Total a Pagar: R${total_com_impostos}")
                                            print(30 * "--")
                                           
                                            print(" ")                
                                            print("Obrigado pela preferencia. Volte sempre...")
                                            print(" ")
                                            break
                                            
                                        else:
                                            print(30 * "--")
                                            print("Saldo insuficiente para realizar o pagamento. Tente outra forma de pagamento.")
                                            continue
                                        
                                    elif forma_pagamento == 2 or forma_pagamento == 3:
                                        print(" ")
                                        saldo_PixCartaoVoucher = float(input("Insira aqui o saldo existente no seu cartão (caso o saldo seja menor que o valor total da compra, o pagamento não podera ser efetuado): "))
                                        
                                        if saldo_PixCartaoVoucher >= total_com_impostos or saldo_PixCartaoVoucher == total_com_impostos:
                                           
                                            troco = qt_dinheiro - total_com_impostos
                                            imposto_nacional = total_compra * 0.05
                                            imposto_estadual = total_compra * 0.08
                                            imposto_municipal = total_compra * 0.12
                                            total_impostos = imposto_nacional + imposto_estadual + imposto_municipal
                                            total_com_impostos = total_compra + total_impostos
                                           
                                            print(30 * "--")
                                            print("---NOTA FISCAL---")
                                            print("-PRODUTOS-")
                                            for i in carrinho:
                                                print(f"- {i[0]}: R${i[1]}")
                                                print(f"Valor total da compra: R${total_compra}")
                                                print(" ")
                                            print(f"Valor do imposto nacional: {imposto_nacional}")
                                            print(f"Valor do imposto estadual: {imposto_estadual}")
                                            print(f"Valor do imposto municipal: {imposto_municipal}")
                                            print(" ")
                                            print(f"Troco: {troco}")
                                            print(f"Total de Impostos: R${total_impostos}")
                                            print(f"Total a Pagar: R${total_com_impostos}")
                                            print(30 * "--")
                                           
                                            print(" ")                
                                            print("Obrigado pela preferencia. Volte sempre...")
                                            print(" ")

                                            carrinho.clear
                                            total_compra = 0
                                            break
                                            
                                        else:
                                            print(30 * "--")
                                            print("Saldo insuficiente para realizar o pagamento. Tente outra forma de pagamento.")
                                            continue

    elif tipo_usuario == 1:

        matricula_do_funcionario = int(input("Insira aqui seu número de matrícula: "))
        nome_do_funcionario = input("Insira aqui seu nome: ")
        data_de_nascimento = input("Insira aqui sua data de nascimento: ")
        cpf_funcionario = input("Insira seu CPF: ")

        while True:
            
            print(30 * "--")
            print("---MENU DO FUNCIONÁRIO---")
            print("- Consultar estoque do mercado (1)")
            print("- Adicionar novo produto ao estoque (2)")
            print("- Remover produto do estoque (3)")
            print("- Voltar a seleção de usuários (0)")
            print(" ")

            opcao_funcionario = int(input("Insira aqui a operação que deseja realizar: "))
            print(30 * "--")

            if opcao_funcionario == 0:
                print(" ")
                print("Voltando para a escolha de usuários...")
                print(" ")
                break
            
            elif opcao_funcionario == 1:
                print(" ")
                print("---ESTOQUE---")
                print(" ")
                print("---PRODUTOS DE HIGIENE---")
                for produto in higiene:
                    print(f"{produto[0]}/Preço: R${produto[1]}/Código: {produto[2]}")
                    print(" ")
                print("---PRODUTOS DE LIMPEZA---")
                for produto in limpeza:
                    print(f"{produto[0]}/Preço: R${produto[1]}/Código: {produto[2]}")
                    print(" ")
                print("---DOCES---")
                for produto in doces:
                    print(f"{produto[0]}/Preço: R${produto[1]}/Código: {produto[2]}")
                    print(" ")
                print("---GRÃOS---")
                for produto in graos:
                    print(f"{produto[0]}/Preço: R${produto[1]}/Código: {produto[2]}")
                    print(" ")
                print("---CARNES---")
                for produto in carnes:
                    print(f"{produto[0]}/Preço: R${produto[1]}/Código: {produto[2]}")
                    print(" ")
                print("---PRODUTOS GERAIS---")
                for produto in gerais:
                    print(f"{produto[0]}/Preço: R${produto[1]}/Código: {produto[2]}")
                    print(" ")
                print("---BEBIDAS---")
                for produto in bebidas:
                    print(f"{produto[0]}/Preço: R${produto[1]}/Código: {produto[2]}")
                    print(" ")
                print("---HORTIFRUTI---")
                for produto in hortifruti:
                    print(f"{produto[0]}/Preço: R${produto[1]}/Código: {produto[2]}")
                    print(" ")
               
            elif opcao_funcionario == 2:
                while True:
                    print(30 * "--")
                    print("---ADICIONAR NOVO PRODUTO AO ESTOQUE---")
                    print("- Higiene (1)")
                    print("- Limpeza (2)")
                    print("- Doces (3)")
                    print("- Grãos (4)")
                    print("- Gerais (5)")
                    print("- Carnes (6)")
                    print("- Bebidas (7)")
                    print("- Frutas, Legumes e Vegetais (8)")
                    print("- Voltar para menu de funcionário (0)")
                    print(" ")
                
                    add_produto = int(input("Insira aqui o número correspondente a seção que você quer adicionar um produto: "))
                    print(30 * "--")
                    
                    if add_produto == 0:
                        print(" ")
                        print("Voltando ao menu de usuário...")
                        print(" ")
                        break
                    
                    elif add_produto == 1:
                        nome_produto = input("Insira o nome do novo produto que deseja adicionar: ")
                        preco_produto = float(input("Insira o preço do produto: "))
                        codigo_produto = int(input("Inisira o código do produto( de 103 a 199): "))
                        
                        if nome_produto in higiene:
                            print("PRODUTO JÁ ESTÁ PRESENTE NO ESTOQUE.")
                        else:
                            higiene.append([nome_produto,preco_produto,codigo_produto])
                            print(" ")
                            print("PRODUTO ADICIONADO AO ESTOQUE.")
                            
                    elif add_produto == 2:
                        nome_produto = input("Insira o nome do novo produto que deseja adicionar: ")
                        preco_produto = float(input("Insira o preço do produto: "))
                        codigo_produto = int(input("Inisira o código do produto( de 203 a 299): "))
                        
                        if nome_produto in limpeza:
                            print("PRODUTO JÁ ESTÁ PRESENTE NO ESTOQUE.")
                        else:
                            limpeza.append([nome_produto,preco_produto,codigo_produto])
                            print(" ")
                            print("PRODUTO ADICIONADO AO ESTOQUE.")
                            
                    elif add_produto == 3:
                        nome_produto = input("Insira o nome do novo produto que deseja adicionar: ")
                        preco_produto = float(input("Insira o preço do produto: "))
                        codigo_produto = int(input("Inisira o código do produto( de 303 a 399): "))
                        
                        if nome_produto in doces:
                            print("PRODUTO JÁ ESTÁ PRESENTE NO ESTOQUE.")
                        else:
                            doces.append([nome_produto,preco_produto,codigo_produto])
                            print(" ")
                            print("PRODUTO ADICIONADO AO ESTOQUE.")
                            
                    elif add_produto == 4:
                        nome_produto = input("Insira o nome do novo produto que deseja adicionar: ")
                        preco_produto = float(input("Insira o preço do produto: "))
                        codigo_produto = int(input("Inisira o código do produto( de 403 a 499): "))
                        
                        if nome_produto in graos:
                            print("PRODUTO JÁ ESTÁ PRESENTE NO ESTOQUE.")
                        else:
                            graos.append([nome_produto,preco_produto,codigo_produto])
                            print(" ")
                            print("PRODUTO ADICIONADO AO ESTOQUE.")
                            
                    elif add_produto == 5:
                        nome_produto = input("Insira o nome do novo produto que deseja adicionar: ")
                        preco_produto = float(input("Insira o preço do produto: "))
                        codigo_produto = int(input("Inisira o código do produto( de 503 a 599): "))
                        
                        if nome_produto in gerais:
                            print("PRODUTO JÁ ESTÁ PRESENTE NO ESTOQUE.")
                        else:
                            gerais.append([nome_produto,preco_produto,codigo_produto])
                            print(" ")
                            print("PRODUTO ADICIONADO AO ESTOQUE.")
                            
                    elif add_produto == 6:
                        nome_produto = input("Insira o nome do novo produto que deseja adicionar: ")
                        preco_produto = float(input("Insira o preço do produto: "))
                        codigo_produto = int(input("Inisira o código do produto( de 603 a 699): "))
                        
                        if nome_produto in carnes:
                            print("PRODUTO JÁ ESTÁ PRESENTE NO ESTOQUE.")
                        else:
                            carnes.append([nome_produto,preco_produto,codigo_produto])
                            print(" ")
                            print("PRODUTO ADICIONADO AO ESTOQUE.")
                            
                    elif add_produto == 7:
                        nome_produto = input("Insira o nome do novo produto que deseja adicionar: ")
                        preco_produto = float(input("Insira o preço do produto: "))
                        codigo_produto = int(input("Inisira o código do produto( de 703 a 799): "))
                        
                        if nome_produto in bebidas:
                            print("PRODUTO JÁ ESTÁ PRESENTE NO ESTOQUE.")
                        else:
                            bebidas.append([nome_produto,preco_produto,codigo_produto])
                            print(" ")
                            print("PRODUTO ADICIONADO AO ESTOQUE.")
                            
                    elif add_produto == 8:
                        nome_produto = input("Insira o nome do novo produto que deseja adicionar: ")
                        preco_produto = float(input("Insira o preço do produto: "))
                        codigo_produto = int(input("Inisira o código do produto( de 803 a 899): "))
                        
                        if nome_produto in hortifruti:
                            print("PRODUTO JÁ ESTÁ PRESENTE NO ESTOQUE.")
                        else:
                            hortifruti.append([nome_produto,preco_produto,codigo_produto])
                            print(" ")
                            print("PRODUTO ADICIONADO AO ESTOQUE.")
                            
            elif opcao_funcionario == 3:
                print(" ")
                print("---ESTOQUE---")
                print(" ")
                print("---PRODUTOS DE HIGIENE---")
                for produto in higiene:
                    print(f"{produto[0]}/Preço: R${produto[1]}/Código: {produto[2]}")
                    print(" ")
                print("---PRODUTOS DE LIMPEZA---")
                for produto in limpeza:
                    print(f"{produto[0]}/Preço: R${produto[1]}/Código: {produto[2]}")
                    print(" ")
                print("---DOCES---")
                for produto in doces:
                    print(f"{produto[0]}/Preço: R${produto[1]}/Código: {produto[2]}")
                    print(" ")
                print("---GRÃOS---")
                for produto in graos:
                    print(f"{produto[0]}/Preço: R${produto[1]}/Código: {produto[2]}")
                    print(" ")
                print("---CARNES---")
                for produto in carnes:
                    print(f"{produto[0]}/Preço: R${produto[1]}/Código: {produto[2]}")
                    print(" ")
                print("---PRODUTOS GERAIS---")
                for produto in gerais:
                    print(f"{produto[0]}/Preço: R${produto[1]}/Código: {produto[2]}")
                    print(" ")
                print("---BEBIDAS---")
                for produto in bebidas:
                    print(f"{produto[0]}/Preço: R${produto[1]}/Código: {produto[2]}")
                    print(" ")
                print("---HORTIFRUTI---")
                for produto in hortifruti:
                    print(f"{produto[0]}/Preço: R${produto[1]}/Código: {produto[2]}")
                    print(" ")
                    
                remover_estoque = int(input("insira aqui o código do produto que deseja remover do estoque: "))
                
                if remover_estoque >= 100 or remover_estoque <= 199:
                    produto_remover = False
                    for item in higiene:
                        if item[2] == remover_estoque:
                            higiene.remove(item)
                            produto_remover = True
                            print(" ")
                            print(f"{item[0]} FOI REMOVIDO DO ESTOQUE DE HIGIENE.")
                            print(" ")
                            break
                    
                if remover_estoque >= 200 or remover_estoque <= 299:
                    produto_remover = False
                    for item in limpeza:
                        if item[2] == remover_estoque:
                            limpeza.remove(item)
                            produto_remover = True
                            print(" ")
                            print(f"{item[0]} FOI REMOVIDO DO ESTOQUE DE LIMPEZA.")
                            print(" ")
                            break
                    
                if remover_estoque >= 300 or remover_estoque <= 399:
                    produto_remover = False
                    for item in doces:
                        if item[2] == remover_estoque:
                            doces.remove(item)
                            produto_remover = True
                            print(" ")
                            print(f"{item[0]} FOI REMOVIDO DO ESTOQUE DE DOCES.")
                            print(" ")
                            break
                    
                if remover_estoque >= 400 or remover_estoque <= 499:
                    produto_remover = False
                    for item in graos:
                        if item[2] == remover_estoque:
                            graos.remove(item)
                            produto_remover = True
                            print(" ")
                            print(f"{item[0]} FOI REMOVIDO DO ESTOQUE DE GRÃOS.")
                            print(" ")
                            break
                    
                if remover_estoque >= 500 or remover_estoque <= 599:
                    produto_remover = False
                    for item in gerais:
                        if item[2] == remover_estoque:
                            gerais.remove(item)
                            produto_remover = True
                            print(" ")
                            print(f"{item[0]} FOI REMOVIDO DO ESTOQUE DE GERAIS.")
                            print(" ")
                            break
                    
                if remover_estoque >= 600 or remover_estoque <= 699:
                    produto_remover = False
                    for item in carnes:
                        if item[2] == remover_estoque:
                            carnes.remove(item)
                            produto_remover = True
                            print(" ")
                            print(f"{item[0]} FOI REMOVIDO DO ESTOQUE DE CARNES.")
                            print(" ")
                            break
                        
                if remover_estoque >= 700 or remover_estoque <= 799:
                    produto_remover = False
                    for item in bebidas:
                        if item[2] == remover_estoque:
                            bebidas.remove(item)
                            produto_remover = True
                            print(" ")
                            print(f"{item[0]} FOI REMOVIDO DO ESTOQUE DE BEBIDAS.")
                            print(" ")
                            break
                       
                if remover_estoque >= 800 or remover_estoque <= 899:
                    produto_remover = False
                    for item in hortifruti:
                        if item[2] == remover_estoque:
                            hortifruti.remove(item)
                            produto_remover = True
                            print(" ")
                            print(f"{item[0]} FOI REMOVIDO DO ESTOQUE DE HORTIFRUTI.")
                            print(" ")
                            break
                       
                else:
                    print(" ")
                    print("CÓDIGO INVÁLIDO.")
                    print(" ")