class Board:

    array = [0]

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.array=[["."] * self.width for _ in range(self.height)]
    
    def printBoard(self):
        for row in self.array:
            print(" ".join(str(cell) for cell in row))
        return 0

    def playAGo(self, x:int, y:int, user:str):
        if not (user == "X" or user == "0"):
            print("somehow you've passed me a non 0 or X, so I am going to stop here. you've passed me ", user)
            return -1
        else :
            self.array[x][y] = user
            return 0

    def checkIfAlreadyPlayed(self, x:int, y:int):
        if ( self.array[x][y] == "."): #good condition i.e it still to be taken
            return 0
        else:
            return -1

    def checkWhatsLeft(self):
        availableSpaces = []
        for y in range(self.height):
            for x in range(self.width):
                value = self.array[y][x]
                if value == ".":
                    #print("Found dot at (", x, " ", y, ")")
                    availableSpaces.append([x,y])
        #print(availableSpaces)
        return availableSpaces

    def checkWinCondition(self):
        #either win by 1 of the rows
        for y in range(self.height): #row by row
            rowsValue = []
            for x in range(self.width): 
                rowsValue.append(self.array[y][x]) #add all of the values in this row to the list
            if all(suit == "X" for suit in rowsValue): #check if the list is just x
                print("X has won!!! by getting a row")
                return 1
            elif all(suit == "0" for suit in rowsValue): #check if the list is just 0
                print("0 has won!!! by getting a row")
                return 1

        #1 of the 3x verticals
        for y in range(self.width): #column by column
            rowsValue = []
            for x in range(self.height): 
                rowsValue.append(self.array[x][y]) 
            if all(suit == "X" for suit in rowsValue):
                print("X has won!!! by getting a column")
                return 1
            elif all(suit == "0" for suit in rowsValue):
                print("0 has won!!! by getting a column")
                return 1
        
        #1 of the diagonals
        diagonalValues = []
        for y in range(self.height): #row by row
            for x in range(self.width): #column by column
                if(x == y):
                    diagonalValues.append(self.array[x][y]) 
        if all(suit == "X" for suit in diagonalValues):
            print("X has won!!! with a diagonalValue")
            return 1
        elif all(suit == "0" for suit in diagonalValues):
            print("0 has won!!! with a diagonal")
            return 1

        #the other diagonal
        otherDiagonalValues = []
        for y in range(self.height): #row by row
            for x in range(self.width): #column by column
                if(x == (self.height-y-1)):
                    otherDiagonalValues.append(self.array[x][y]) 
        if all(suit == "X" for suit in otherDiagonalValues):
            print("X has won!!! with an other diagonal")
            return 1
        elif all(suit == "0" for suit in otherDiagonalValues):
            print("0 has won!!! with an other diagonal")
            return 1
        return 0


