#criar um sitema simples de agendamento de livros
#tem q ter uma classe de livros e uma biblioteca

from biblioteca import Biblioteca
from livros import Livro

def ExibirMenu():
    print("1 - ADICIONAR LIVRO")
    print("2 - CONSULTAR DETALHES DO LIVRO")
    print("3 - EMPRESTAR UM LIVRO")
    print("4 - LISTAR TODOS OS LIVROS DA BIBLIOTECA")
    print("5 - DEVOLVER LIVRO")
    print("0 - SAIR")

biblioteca = Biblioteca()


while True:
    ExibirMenu()
    opcao = int (input("Digite a opção desejada: "))
    
    if opcao == 0:
         print("Bye Bye.....")
         break
    
    elif opcao == 1:
          titulo = input("Digite o titulo do livro: ")
          autor = input("Digite o autor do livro: ")
          livro = Livro(titulo, autor)
          biblioteca.AdicionarLivro(livro)

    elif opcao == 2:
         titulo = input("Digite o titulo que quer buscar: ")
         detalhe = biblioteca.ConsultarDetalhe(titulo)
         print(detalhe)

    elif opcao == 3:
         titulo = input("Digite o titulo que quer buscar: ")
         biblioteca.EmprestarLivro(titulo)

    elif opcao == 4:
         biblioteca.ListarLivros()

    elif opcao == 5:
         titulo = input("Digite o titulo que quer buscar: ")
         biblioteca.DevolverLivro(titulo)