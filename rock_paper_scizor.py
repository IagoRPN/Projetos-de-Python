from operator import truediv
import random

def play():
    user = input("'r' for rock, 'p' for paper and 's' for scizor: ").lower()
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'It\'s a tie'

    if is_win(user, computer):
        return 'You won'

    return 'You lose'

def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True
    return False


choice = True
while choice:
    print(play())
    enter = input('Play again? (y/n)').lower()
    if enter == 'y': 
        choice = True
    else:
        choice = False
        print("Bye!")