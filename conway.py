# Conways game of life 
import random, time, copy
WIDTH = 100
HEIGHT = 20
# Create a List of all of the cells:
nextCell = []

# prepopulate the board
def populateBoard():
    nextCells = []
    for y in range(HEIGHT):
        row = [] # Create a new row
        for x in range (WIDTH):
            if(random.randint(0,1) == 0):
                row.append('#') # living cell
            else:
                row.append('_') # dead cell
        
        nextCells.append(row)
    return nextCells

def populateBoardWithGlider():
    nextCells = []
    gliderTuple = ((1, 0), (2, 1), (0, 2), (1, 2), (2, 2))
    for y in range(HEIGHT):
        row = [] # Create a new row
        for x in range (WIDTH):
            if((x,y) in gliderTuple):
                row.append('#') # living cell
            else:
                row.append(' ') # dead cell
        
        nextCells.append(row)
    return nextCells



def printBoard(board):
    print ('\n\n\n\n\n\n')
    for row in board:
        for cell in row:
            print(cell, end='') 
        print()

def countNeighbors(board, x, y):
    # % makes sure the board wraps
    leftCord = (x - 1) % WIDTH
    rightCord = (x + 1) % WIDTH
    bottomCord = (y + 1) % HEIGHT
    topCord = (y - 1) % HEIGHT
    
    neighbors = 0
    if(board[topCord][x] == '#'): # top
        neighbors+=1
    if(board[topCord][rightCord]== '#'): # top-right
        neighbors+=1
    if(board[y][rightCord]== '#'): # right
        neighbors+=1
    if(board[bottomCord][rightCord] == '#'): # bottom-right
        neighbors+=1
    if(board[bottomCord][x] == '#'): # bottom
        neighbors+=1
    if(board[bottomCord][leftCord] == '#'): # bottom-left
        neighbors+=1
    if(board[y][leftCord] == '#'): # left
        neighbors+=1
    if(board[topCord][leftCord] == '#'): # top-left
        neighbors+=1

    return neighbors

def calculateNextTurn(board):
    nextBoard = copy.deepcopy(board)
    for y, row in enumerate(board):
        for x, cell in enumerate(row):
            numNeighbors = countNeighbors(board, x, y)
            staysAlive = cell == '#' and numNeighbors == 2 or numNeighbors == 3
            comesAlive = cell != '#' and numNeighbors == 3
            if(staysAlive or comesAlive):
                nextBoard[y][x] = '#' 
            else:
                nextBoard[y][x] = ' '
    return nextBoard


# user input loop
while True:
    print('How would you like to start the board?\n \
            (g)lider or (r)andom', end=':')
    userSelection = input()
    if(userSelection == 'g'):
        currentCells = populateBoardWithGlider()
        break
    elif(userSelection == 'r'):  
        currentCells = populateBoard()
        break
    else:
        print('not a valid Selection')


# main loop
while True:
    printBoard(currentCells)
    currentCells = calculateNextTurn(currentCells)
    time.sleep(0.5)
