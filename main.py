from Board import Board

#Starting the game
print("Hello, lets play naughts and crosses")

#todo add the ability to input the nxn board.
print("Generating the board")
gameBoard = Board(3,3)

usersSuit = ""

def setUpGame():
    global usersSuit
    while usersSuit not in ("X", "0"):
        usersSuit = input("Do you want to be 0 or X? ")

    print("Nice, you will be", usersSuit, "and I will be the other one")

def playersGo():
    usersX = input("Pick cell X ")
    usersY = input("Pick cell y ")
    gameBoard.playAGo(int(usersX), int(usersY), usersSuit)
    gameBoard.printBoard()

setUpGame()

while(1 != 2) :
    playersGo()

