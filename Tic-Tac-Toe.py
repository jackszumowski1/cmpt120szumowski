# CMPT 120 Intro to Programming
# Lab #6 –Lists and Error Handling
# Author: Jack Szumowski
# Created: 2019-08-04
symbol = [ " ", "X", "O" ]

def printRow(row):
    
    # initialize output to the left border
    output = "|"

    # for each square in the row...
    for i in range(3):
        
        # add to output the symbol for this square followed by a border
        output = output + " " + symbol[row[i]] + " |"
        
    # print the completed output for this rowpass
    print(output)
    
def printBoard(board):
    
    # print the top border
    print("+-----------+")
          
    # for each row in the board...
    for i in range(3):
          
        # print the row
        printRow(board[i])
          
        # print the next borderpass
        print("+-----------+")
    
            
           
def markBoard(board, row, col, player):
    # check to see whether the desired square is blank
    # if so,set it to the player numberpass

    if board[row][col] == 0:
        board[row][col] = player
    
        
            
        
    
def getPlayerMove():
    # prompt the user separately for the row and column numbers
    row = int(input("enter a row (1-3): "))
    col = int(input("enter a col (1-3): "))
    return (row - 1, col - 1)
    # then return that row and column instead of (0,0)

    
def hasBlanks(board):
    # for each row in the board...
    # for each square in the row...
    # check whether the square is blank
    # if so, return True

    # JA: this does not work because board has lists, not numbers
    for row in board:
        if 0 in row:
#    if 0 in board or " " in board:
        
            return True
    

#    else:
    return False # if no square is blank
    


def main():
        
    # TODO replace this with a three-by-three matrix of zeros
    
    board = [[0,0,0],
            [0,0,0],
            [0,0,0]]
    
    count = 0
    player = 1
    while hasBlanks(board) or count < 10:
        count += 1
        printBoard(board)
        row,col = getPlayerMove()
        markBoard(board,row,col,player)
        # switch player for next turn
        player = player % 2 + 1
    # JA: You have to print the board again
    printBoard(board)
        

main()
