class Barbearia:
    def __init__(self):
        self.cliente = []

    def AgendarCliente(self,cliente):
        self.cliente.append(cliente)
      
    def BuscarAgendamento(self, nome):
        for cliente in self.cliente:
            if cliente.nome == nome:
                return cliente
        return None  

    def CancelarAgendamento(self, nome):
        cliente = self.BuscarAgendamento(nome)
        if cliente:
            if cliente.status == "AGENDADO.":
                cliente.status = "CANCELADO."
                print("AGENDAMENTO CANCELADO COM SUCESSO!!!")
            else:
                print("ESTE AGENDAMENTO JA ESTÁ CANCELADO.")
        else:
            print("AGENDAMENTO NÃO ENCONTRADO.")

    def ConsultarAgendamento(self,nome):
        agendamento = self.BuscarAgendamento(nome)
        if agendamento:
            return agendamento
        else:
            print("AGENDAMENTO NÃO ENCONTRADO.")
