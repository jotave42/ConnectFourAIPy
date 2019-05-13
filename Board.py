class Board():
    gameBoard=[]
    __lastRow = 6
    width = 7
    height = 6
    turn= 1
    def __init__(self, gameBordToCopy = None,turnCopy = None):
        self.gameBoard=[]
        if(turnCopy!=None):
            self.turn = turnCopy
        if(gameBordToCopy):
            for row in range(6):
                cols=[]
                for col in range(7):
                    cols.append(gameBordToCopy[row][col])
                self.gameBoard.append(cols)
        else:
            for row in range(6):
                cols =[]
                for col  in range(7):
                    cols.append(0)
                self.gameBoard.append(cols)

    def addable(self,col):
        i = 0
        while(i < 6 and self.gameBoard[i][col] == 0  ):
            i+=1
        self.__lastRow = i -1
        if(i != 0 ):
            return True
        return False

    def addPieceSumulation(self, col , player1Icon,player2Icon):
        if(self.addable(col)):
            if(self.getTurn()==1):
                self.gameBoard[self.__lastRow][col] = player1Icon
                self.setTurn(0)
            else:
                self.gameBoard[self.__lastRow][col] = player2Icon
                self.setTurn(1)
            return self.__lastRow
        else:
            return -1
    
    def addPiece(self, col , playerIcon):
        if(self.addable(col)):
            self.gameBoard[self.__lastRow][col] = playerIcon
            if(self.getTurn()==1):
                self.setTurn(0)
            else:
                self.setTurn(1)
            return self.__lastRow
        else:
            return -1
    def showBord(self):
        for row  in self.gameBoard:
            print(row)

    def showBord(self,player1Icon,player2Icon):
        print("\n=================")
        for row  in self.gameBoard:
            line = "[ "
            for col in row:
                if(col == player1Icon):
                    line += '\033[31m'+col+'\033[0m'+" "
                elif (col == player2Icon):
                    line +=  '\033[32m'+col+'\033[0m'+" "
                else:
                    line += str(col)+" "
            line += "]"
            print(line)
        print("=================\n")
    def checkVerticalStreaks(self, playerIcon):
        for colum in range(7):
            currentStreak = 0
            for row in range(6):
                if (self.gameBoard[row][colum] == playerIcon):
                    currentStreak += 1
                    if (currentStreak == 4):
                        return True
                else:
                    currentStreak = 0
        return False

    def checkHorizontalStreaks(self, playerIcon):
        for row in self.gameBoard:
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
                if self.gameBoard[row][colum] == playerIcon and self.gameBoard[row+1][colum-1] == playerIcon and self.gameBoard[row+2][colum-2] == playerIcon and self.gameBoard[row+3][colum-3] == playerIcon: 
                    return True
        return False

    def checkSDiagonalStreaks(self, playerIcon):
        for row in range(3):
            for colum in range(4):
                if self.gameBoard[row][colum] == playerIcon and self.gameBoard[row+1][colum+1] == playerIcon and self.gameBoard[row+2][colum+2] == playerIcon and self.gameBoard[row+3][colum+3] == playerIcon: 
                    return True
        return False

    def chekWin(self, playerIcon):
        win = self.checkVerticalStreaks(playerIcon) or self.checkHorizontalStreaks(playerIcon) or self.checkMDiagonalStreaks( playerIcon) or self.checkSDiagonalStreaks(playerIcon)
        return win
    def chekTie(self):
        for row in range(6):
            for col in range(7):
                if (self.gameBoard[row][col]==0):
                    return False
        return True

    def chekFinal(self, player1Icon, player2Icon):
        if(self.chekWin(player2Icon)):
            return 2
        elif(self.chekWin(player1Icon)):
            return 1
        elif(self.chekTie()):
            return 0
        else:
            return -1

    def getLastRow(self):
        return self.__lastRow


    def getTurn(self):
        return(self.turn)

    def setTurn(self,vl):
        self.turn = vl
