class Board():
    gameBord=[]
    __lastRow = 6
    def __init__(self, gameBordToCopy):
        for row in range(6):
            cols=[]
            for col in range(7):
                cols.append(gameBordToCopy[row],[col])
            self.gameBord(cols)

    def __init__(self):
        self.gameBord=[]
        for row in range(6):
            cols =[]
            for col  in range(7):
                cols.append(0)
            self.gameBord(cols)
    
    def addable(self,col):
        i = 0
        while(i < 6 and self.gameBord[i][col] == 0  ):
            i+=1

        self.__lastRow = i
        if(i != 0 ):
            return True
        return False
    def addPiece(self, col , player):
        if(self.addable(col)):
            self.gameBord[self.__lastRow][col] = player.icon
    
    def showBord(self):
        for row  in self.Board:
            print(row)
            

    
