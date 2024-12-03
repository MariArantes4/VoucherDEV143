data = (input("Digite uma data: "))

dia = int(data[0:2])
mes = int(data[3:5])
ano = int(data[6:10])

if data[2]== "/" and data[5] == "/":

 if(dia <= 0 or dia >= 32):
    print ("data invalida")

if (mes <= 0 or mes >= 13):
    print ("data invalida")

if (ano <= 0 or ano>= 9999):
    print("data invalida")

else:
    print("data invalida")