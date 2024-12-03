class Biblioteca:
    def __init__(self):
        self.livros = []

    def AdicionarLivro(self, livro):
        self.livros.append(livro)
       
    def BuscarLivro(self, titulo):
        for i in self.livros:
            if i.titulo == titulo:
                return i

    def ConsultarDetalhe(self, titulo):
        livro = self.BuscarLivro(titulo)

        if livro:
            return livro
        else:
            print("Livro não encontrado!!!")

    def EmprestarLivro(self, titulo):
        livro = self.BuscarLivro(titulo)

        if livro:
            if livro.emprestado == False:
                print ("Emprestimo realizado")
                livro.emprestado = True
            else:
                print("Livro já emprestado")
        else:
            print("Livro não encontrado")

    def ListarLivros(self):
        for i in self.livros:
            print(i)
            
    def DevolverLivro(self, titulo):
        livro = self.BuscarLivro(titulo)

        if livro:
            if livro.emprestado == True:
                print("Devolvido com sucesso")
                livro.emprestado == False
            else:
                print("O livro não esta emprestado para ir para devolução")
        else:
            print("Livro não encontrado")