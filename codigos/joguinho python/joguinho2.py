nome= input("digite seu nome:")
ano_de_nascimento=int(input("digite o ano que você nasceu:"))
ano_atual=int(input("digite o ano atual:"))
idade= ano_atual - ano_de_nascimento
if idade >= 18:
    print (nome,"sua entrada foi permitida")
else:
    print (nome, "sua idade não foi permitida")