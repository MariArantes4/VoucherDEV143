class Cliente:
    def __init__(self,nome,data,hora,serviço):
        self.nome = nome
        self.data = data
        self.hora = hora 
        self.serviço = serviço
        self.status = "Agendado"


    def __str__(self):
         status = "AGENDADO"
         return f"Nome: {self.nome}/Data: {self.data}/Hora: {self.hora}/Serviço: {self.serviço} - {status}"
