class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.emprestado = True


    def __str__(self):
        status = "disponivel"
        if self.emprestado == True:
            status = "Emprestado"
        return f"Titulo: {self.titulo}/Autor: {self.autor} - {status}"
