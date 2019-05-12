from ConnectFour import *
from termcolor import colored, cprint
class Board():
    gameBord=[]
    __lastRow = 6
    width = 7
    height = 6


    def __init__(self, gameBordToCopy = None):
        self.gameBord=[]
        self.turn = getTurn()
        if(gameBordToCopy):
            for row in range(self.height):
                cols=[]
                for col in range(self.width):
                    cols.append(gameBordToCopy[row][col])
                self.gameBord.append(cols)
        else:
            for row in range(self.height):
                cols =[]
                for col  in range(self.width):
                    cols.append(0)
                self.gameBord.append(cols)
    
    def addable(self,col):
        i = 0
        while(i < self.height and self.gameBord[i][col] == 0  ):
            i+=1
        self.__lastRow = i
        if(i != 0 ):
            return True
        return False

    def addPiece(self, col , playerIcon):
        if(self.addable(col)):
            self.gameBord[self.__lastRow-1][col] = playerIcon
            return self.__lastRow
        else:
            return -1
    
    def showBord(self):
        for row  in self.gameBord:
            print(row)

    def showBord(self,player1Icon,player2Icon):
        for row  in self.gameBord:
            line = "[ "
            for col in row:
                if(col == player1Icon):
                    line += colored(col, 'red')+" "
                elif (col == player2Icon):
                    line += colored(col, 'green')+" "
                else:
                    line += colored(col, 'white')+" "
            line += "]"
            print(line)

    def checkVerticalStreaks(self, playerIcon):
        for colum in range(self.width):
            currentStreak = 0
            for row in range(self.height):
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
            for colum in range(self.width):
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
        win = self.checkVerticalStreaks(playerIcon) or self.checkHorizontalStreaks(playerIcon) or self.checkMDiagonalStreaks( playerIcon) or self.checkSDiagonalStreaks(playerIcon)
        return win

    def getLastRow(self):
        return self.__lastRow
