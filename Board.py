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
            print("somehow you've passed me a non 0 or X, so I am going to stop here")
            return -1
        else :
            self.array[x][y] = user
            return 0