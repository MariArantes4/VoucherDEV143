cont= 0
nome_certo = "rafael" 
nome_certo2 = "RAFAEL"
nome_certo3 = "Rafael" 

while True:
   nome= input("digite um nome:")
   cont+=1
   if nome == nome_certo or nome== nome_certo2 or nome==nome_certo3:
      break
  
print("contador:", cont)