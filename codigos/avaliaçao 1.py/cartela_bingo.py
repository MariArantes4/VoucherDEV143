import random

class BingoCard:
    def __init__(self):
        ranges = [
            range(1, 16),  # B
            range(16, 31), # I
            range(31, 46), # N
            range(46, 61), # G
            range(61, 76)  # O
        ]
        self.card = [[random.choice(number_range) for _ in range(5)] for number_range in ranges]
        self.card[2][2] = 0  
        self.marked = [[False] * 5 for _ in range(5)]
        self.marked[2][2] = True  

    def check_bingo(self):
        for row in self.marked:
            if all(row):
                return True

        for col in range(5):
            if all(self.marked[row][col] for row in range(5)):
                return True

        if all(self.marked[i][i] for i in range(5)) or all(self.marked[i][4-i] for i in range(5)):
            return True

        return False

    def display_marked_card(self):
        headers = [' B', ' I', ' N', ' G', ' O']
        print(" ".join(headers))
        for row in range(5):
            for col in range(5):
                if self.card[col][row] == 0 or self.marked[col][row]:
                    print(" X", end=" ")
                else:
                    print(f"{self.card[col][row]:2}", end=" ")
            print()

bingo_card = BingoCard()

bingo_card.display_marked_card()

while True:
    number = int(input("Digite os números já sorteados: "))
    for col in range(5):
        for row in range(5):
            if bingo_card.card[col][row] == number:
                bingo_card.marked[col][row] = True
    
    bingo_card.display_marked_card()
    
    if bingo_card.check_bingo():
        print("Bingo!")
        break

