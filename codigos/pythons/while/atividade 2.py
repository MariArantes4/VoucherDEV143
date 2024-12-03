while True:
    usuario = input("digite um nome de usuario: ")
    senha = input("digite uma senha: ")
    
    if senha == usuario:
        print("Senha invalida. Senha não pode ser igual ao nome de usuário.")
   
    else: 
       print ("nome e senha validos.")
       break