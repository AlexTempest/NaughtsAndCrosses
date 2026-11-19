from Board import Board
from random import randint

#Starting the game
print("Hello, lets play naughts and crosses")

#todo add the ability to input the nxn board.
print("Generating the board")
gameBoard = Board(3,3)

availableSuits = ["0","X"]
usersSuit = ""
cpuSuit = ""

def setUpGame():
    global usersSuit
    while usersSuit not in ("X", "0"):
        usersSuit = input("Do you want to be 0 or X? ")

    availableSuits.remove(usersSuit)
    cpuSuit = availableSuits[0]
    print("Nice, you will be", usersSuit, "and I will be ", cpuSuit)

def playersGo():
    complete = 1
    while(complete != 0):
        usersX = input("Pick cell X ")
        usersY = input("Pick cell y ")
        if(gameBoard.checkIfAlreadyPlayed(int(usersX), int(usersY)) == -1):
            print("This cell has already been taken, pick another one pal")
        else:
            gameBoard.playAGo(int(usersX), int(usersY), usersSuit)
            gameBoard.printBoard()
            complete = 0
    return 0

def cpuGo():
    possibleMoves = gameBoard.checkWhatsLeft()
    move = possibleMoves[randint(0, len(possibleMoves)-1)]
    gameBoard.playAGo(int(move[0]), int(move[1]), "X") #todo a bug where cpusuit isnt saving
    gameBoard.printBoard()

setUpGame()

gotracker=0

while(gameBoard.checkWinCondition() == 0):
    if gotracker % 2 == 0:
        playersGo() # Even 
    else:
        cpuGo() # Odd
    gotracker += 1

