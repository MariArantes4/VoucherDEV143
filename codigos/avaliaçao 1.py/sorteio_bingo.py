import random

numbers = list(range(1, 76))
random.shuffle(numbers)

drawn_numbers = []

while numbers:
    action = input("Pressione Enter para sortear um número ou digite 'sair' para encerrar: ").strip().lower()
    if action == 'sair':
        print("Encerrando o Sorteio")
        break
  
    number = numbers.pop()
    drawn_numbers.append(number)

    print(f"Número sorteado: {number}")
    print(f"Números sorteados até agora: {drawn_numbers}")

if not numbers:
    print("Todos os números já foram sorteados.")
