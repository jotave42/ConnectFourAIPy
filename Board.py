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
    def addPiece(self, col , playerIcon):
        if(self.addable(col)):
            self.gameBord[self.__lastRow][col] = playerIcon
    
    def showBord(self):
        for row  in self.Board:
            print(row)

    def checkVerticalStreaks(self, playerIcon):
        for colum in range(7):
            currentStreak = 0
            for row in range(6):
                if (self.gameBord[row][colum] == playerIcon):
                    currentStreak += 1
                    if (currentStreak == 4):
                        return True
                else:
                    currentStreak =0

        return False

    def checkHorizontalStreaks(self, playerIcon):
        for row in self.gameBord:
            currentStreak = 0
            for colum in range(7):
                if (row[colum] == playerIcon):
                    currentStreak +=1
                    if (currentStreak == 4):
                        return True
                else:
                    currentStreak = 0
        return False

    def checkMDiagonalStreaks(self, playerIcon):
        for row in range(3):
            for colum in range(3,7,1):
                if self.gameBord[row][colum] == playerIcon and self.gameBord[row+1][colum-1] == playerIcon and self.gameBord[row+2][colum-2] == playerIcon and self.gameBord[row+3][colum-3] == playerIcon: 
                    return True
        return False

    def checkSDiagonalStreaks(self, playerIcon):
        for row in range(3):
            for colum in range(4):
                if self.gameBord[row][colum] == playerIcon and self.gameBord[row+1][colum+1] == playerIcon and self.gameBord[row+2][colum+2] == playerIcon and self.gameBord[row+3][colum+3] == playerIcon: 
                    return True
        return False

    def chekWin(self, playerIcon):
        return checkVerticalStreaks(playerIcon) or checkHorizontalStreaks(playerIcon) or checkMDiagonalStreaks( playerIcon) or checkSDiagonalStreaks(playerIcon)


    
