import os

board = ['-','-','-',
        '-','-','-',
        '-','-','-']

available_numbers = [0,1,2,3,4,5,6,7,8]
win_conditions = [[0,1,2],
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

playerA = 'X'
playerB = 'O'

gameRunning = True

def printBoard(board):
    print(board[0] + '|' + board[1] + '|' + board[2])
    print('-----')
    print(board[3] + '|' + board[4] + '|' + board[5])
    print('-----')
    print(board[6] + '|' + board[7] + '|' + board[8])

def processMove(input,player):
    board[input-1] = player

def checkGame(win_conditions, playerA_moves, playerB_moves):

    if (playerA_moves.sort() in win_conditions):
        print("Player A Wins!!!") 
        return True

    if (playerB_moves.sort() in win_conditions):
        print("Player B Wins!!!")
        return True

    else:
        return False

os.system('CLS')

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
    
    if(checkGame(win_conditions, playerA_moves, playerB_moves)):
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

    if(checkGame(win_conditions, playerA_moves, playerB_moves)):
        break
    
    

