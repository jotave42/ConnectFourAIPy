from termcolor import colored, cprint
class Board():
    gameBord=[]
    __lastRow = 6
    width = 7
    height = 6
    turn= 1
    evaluationTable=[]
    deltaEvaluationTable=[]   
    def __init__(self, gameBordToCopy = None, evaluationTableCopy = None,deltaEvaluationTableCopy = None,turnCopy=None):
        self.gameBoard=[]
        self.evaluationTable=[]
        self.deltaEvaluationTable=[]
        #print("turncopy ------>",turnCopy)
        if(turnCopy!=None):
            self.turn = turnCopy
            #print("turn copiado---->",self.turn)
        if((gameBordToCopy)and(evaluationTableCopy)):
            for row in range(6):
                cols=[]
                colsEvaluation=[]
                colsDeltaEvaluation=[]
                for col in range(7):
                    cols.append(gameBordToCopy[row][col])
                    colsEvaluation.append(evaluationTableCopy[row][col])
                    colsDeltaEvaluation.append(deltaEvaluationTableCopy[row][col])
                self.gameBoard.append(cols)
                self.evaluationTable.append(colsEvaluation)
                self.deltaEvaluationTable.append(colsEvaluation)
        else:
            for row in range(6):
                cols =[]
                for col  in range(7):
                    cols.append(0)
                self.gameBoard.append(cols)
            self.evaluationTable=[]
            self.evaluationTable.append([3, 4, 5, 7, 5, 4, 3])
            self.evaluationTable.append([4, 6, 8, 10, 8, 6, 4])
            self.evaluationTable.append([5, 8, 11, 13, 11, 8, 5])
            self.evaluationTable.append([5, 8, 11, 13, 11, 8, 5])
            self.evaluationTable.append([4, 6, 8, 10, 8, 6, 4])
            self.evaluationTable.append([3, 4, 5, 7, 5, 4, 3])
            self.deltaEvaluationTable =[]
            for i in range(6):
                lin=[0]*7
                self.deltaEvaluationTable.append(lin)
    

    def evaluateContent(self, player1Icon, player2Icon):
        utility = 138
        summ = 0
        for row  in range(6):
            for colum in range(7):
                if(self.gameBoard[row][colum] == player1Icon ):
                    summ -= self.evaluationTable[row][colum]
                elif(self.gameBoard[row][colum] == player2Icon ):
                    summ += self.evaluationTable[row][colum]
        return utility + summ

    def showEvaluation(self):
        print()
        print("=========BEGIN==============")
        print("EVALUATIONTABLE")
        for i in self.evaluationTable:
            print(i)
        print("DELTA_EVALUATIONTABLE")
        for i in self.deltaEvaluationTable:
            print(i)
        print("=========END================")
        print()
    
    def chengEvaluationAtPosition(self, row , col, ai):
            if(self.evaluationTable[row][col] != 0):
                if(ai):
                    self.deltaEvaluationTable[row][col] += 1
                    self.evaluationTable[row][col] += 1
                else:
                    self.deltaEvaluationTable[row][col] -= 1
                    if(self.deltaEvaluationTable[row][col] == -3):
                        self.evaluationTable[row][col]+=3
                        
                    else:    
                        self.evaluationTable[row][col]-=1

    def updateEvaluation(self,row , col , ai):
        self.evaluationTable[row][col] = 0
        self.showEvaluation()
        for i in range(1,4,1):
            if(col + i < 7):
                self.chengEvaluationAtPosition(row, col + i, ai)
            if(col - i >= 0):
                self.chengEvaluationAtPosition(row, col - i, ai)
            if(row + i <  6):
                self.chengEvaluationAtPosition(row + i, col, ai)
            if(row - i >= 0):
                self.chengEvaluationAtPosition(row - i, col, ai)    
            if((col + i < 7) and (row + i <  6)):
                self.chengEvaluationAtPosition(row + i, col + i, ai)
            if((col + i < 7) and (row - i >= 0)):
                self.chengEvaluationAtPosition(row - i, col + i, ai)
            if((col - i >= 0) and (row - i >= 0)):
                self.chengEvaluationAtPosition(row - i, col - i, ai)
            if((col - i >= 0) and (row + i <  6)):
                self.chengEvaluationAtPosition(row + i, col - i, ai)
        self.showEvaluation()



    def addable(self,col):
        i = 0
        while(i < 6 and self.gameBoard[i][col] == 0  ):
            i+=1
        self.__lastRow = i -1
        if(i != 0 ):
            return True
        return False

    def addPieceSumulation(self, col , player1Icon,player2Icon):
        #print("Simulation entrei con---->",self.getTurn())
        if(self.addable(col)):
            if(self.getTurn()==1):
                self.gameBoard[self.__lastRow][col] = player1Icon
                self.setTurn(0)
            else:
                self.gameBoard[self.__lastRow][col] = player2Icon
                self.setTurn(1)
            #print("Simulation SAI con---->",self.getTurn())
            return self.__lastRow
        else:
            return -1
    
    def addPiece(self, col , playerIcon):
        #print(self.getTurn())
        if(self.addable(col)):
            self.gameBoard[self.__lastRow][col] = playerIcon
            if(self.getTurn()==1):
                self.setTurn(0)
            else:
                self.setTurn(1)
            #print(self.getTurn())
            return self.__lastRow
        else:
            return -1
    def showBord(self):
        for row  in self.gameBoard:
            print(row)

    def showBord(self,player1Icon,player2Icon):
        print("\n================================")
        for row  in self.gameBoard:
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
        print("================================\n")
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
                if (self.evaluationTable[row][col]!=0):
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