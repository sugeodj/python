import random

def game(move):
    moves: list = ['rock', 'paper', 'scissors']
    if move in moves:
        answer: str = random.choice(moves)

        if move == answer:
            print('You drawed.')
            return 
        
        elif move == 'Rock' and answer == "Scissors" or move == 'Paper' and answer == 'Rock' or move == 'Scissors' and answer == 'Paper':
            print(f'You: {move}\n CPU: {answer}\n You Won.')
            return

        else:
            print(f'You: {move}\n CPU: {answer}\n You Lost.')
            return


print('Rock, Paper, or Scissors?')        
input: str = input("Your choice: ")

game(input.lower())

        