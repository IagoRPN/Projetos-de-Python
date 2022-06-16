import os

green = "\u001b[32;1m"
blue = "\u001b[34;1m"
reset_color = "\u001b[0m"

board = ['[1]','[2]','[3]',
        '[4]','[5]','[6]',
        '[7]','[8]','[9]']

available_numbers = [0,1,2,3,4,5,6,7,8]
win_conditions = [
                  [0,1,2],
                  [3,4,5],
                  [6,7,8],
                  [0,3,6],
                  [1,4,7],
                  [2,5,8],
                  [0,4,8],
                  [2,4,6]
                  ]

playerA_moves = []
playerB_moves = []

playerA =  green + '[X]' + reset_color
playerB =  blue + '[O]' + reset_color

gameRunning = True

def printBoard(board):
    print(board[0] + board[1] +  board[2])
    print('---------')
    print(board[3] + board[4] + board[5])
    print('---------')
    print(board[6] + board[7] + board[8])

def processMove(input,player):
    board[input-1] = player

def checkGameStatus(win_conditions, playerA_moves, playerB_moves, available_numbers):
    for conditions in range(0, len(win_conditions)):
        #print(conditions)
        check_A = [x for x in playerA_moves if x in win_conditions[conditions]]
        check_B = [x for x in playerB_moves if x in win_conditions[conditions]]

        #print(str(check_A) + '|' + str(win_conditions[conditions]))
        #print(str(check_B) + '|' + str(win_conditions[conditions]))
        
        if (sorted(check_A) == win_conditions[conditions]):
            print('Player A WINS!!!')
            return True
           
        if (sorted(check_B) == win_conditions[conditions]):
            print('Player B WINS!!!')
            return True

    if (available_numbers == []):
        print('Its a Tie!!!') 
        return True

    return False
        

        

    

       
            


        

   

os.system('CLS')
printBoard(board)

while gameRunning:
   
    
    inp = int(input("Player A: Enter a number 1~9: "))
    if (inp >= 1) and (inp <= 9) and (inp - 1 in available_numbers):
        processMove(inp, playerA)
        playerA_moves.append(inp-1)
        available_numbers.remove(inp-1)
        #print(available_numbers)
        os.system('CLS')
        printBoard(board)

    else: 
        print('Please type a valid number!!')
        break
    
    if(checkGameStatus(win_conditions, playerA_moves, playerB_moves, available_numbers)):
        break
        
    inp = int(input("Player B: Enter a number 1~9: "))
    if (inp >= 1) and (inp <= 9) and (inp - 1 in available_numbers):
        processMove(inp, playerB)
        playerB_moves.append(inp-1)
        available_numbers.remove(inp-1)
        #print(available_numbers)
        os.system('CLS')
        printBoard(board)

    else: 
        print('Please type a valid number!!')
        break

    if(checkGameStatus(win_conditions, playerA_moves, playerB_moves, available_numbers)):
        break
    
    

