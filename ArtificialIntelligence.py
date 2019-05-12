from Board import *
import math
class ArtificialIntelligence:
    def __init__(self):
        self.EVALUATIONTABLE = []
        self.EVALUATIONTABLE.append([3, 4, 5, 7, 5, 4, 3])
        self.EVALUATIONTABLE.append([4, 6, 8, 10, 8, 6, 4])
        self.EVALUATIONTABLE.append([5, 8, 11, 13, 11, 8, 5])
        self.EVALUATIONTABLE.append([5, 8, 11, 13, 11, 8, 5])
        self.EVALUATIONTABLE.append([4, 6, 8, 10, 8, 6, 4])
        self.EVALUATIONTABLE.append([3, 4, 5, 7, 5, 4, 3])
        self.DELTA_EVALUATIONTABLE = []
        for i in range(6):
            col = [0]*7
            self.DELTA_EVALUATIONTABLE.append(col)

    def showEvaluation(self):
        print()
        print("=========BEGIN==============")
        print("EVALUATIONTABLE")
        for i in self.EVALUATIONTABLE:
            print(i)
        print("DELTA_EVALUATIONTABLE")
        for i in self.DELTA_EVALUATIONTABLE:
            print(i)
        print("=========END================")
        print()
    def chengEvaluationAtPosition(self, row , col, ai):
                if(ai):
                    self.DELTA_EVALUATIONTABLE[row][col] += 1
                    self.EVALUATIONTABLE[row][col] += 1
                else:
                    self.DELTA_EVALUATIONTABLE[row][col] -= 1
                    if(self.DELTA_EVALUATIONTABLE[row][col] == -3):
                        self.EVALUATIONTABLE[row][col]+=3
                        self.DELTA_EVALUATIONTABLE[row][col] += 3
                    else:    
                        self.EVALUATIONTABLE[row][col]-=1

    def updateEvaluation(self,row , col , ai):
        self.EVALUATIONTABLE[row][col] = 0
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
    def evaluateContent(self, gBorde, player1Icon, player2Icon):
        utility = 138
        summ = 0
        for row  in range(6):
            for colum in range(7):
                if(gBorde[row][colum] == player1Icon ):
                    summ -= self.EVALUATIONTABLE[row][colum]
                elif(gBorde[row][colum] == player2Icon ):
                    summ += self.EVALUATIONTABLE[row][colum]
        return utility + summ

    def minMax(self,gBorde, depth, alph, beta, maximazingPlayer, player1Icon, player2Icon):
        if(depth == 0):
            print("EVALUATE: ",self.evaluateContent(gBorde, player1Icon, player2Icon))
            return self.evaluateContent(gBorde, player1Icon, player2Icon)
        print("MINMAX --->DETPH: ",depth)
        if(maximazingPlayer):
            value = -9000
            for i in range(7):
                board =  Board(gBorde) 
                board.addPiece(i,player1Icon)
                board.showBord(player1Icon,player2Icon)
                value = max(value, self.minMax(board.gameBord, depth-1, alph, beta, False, player1Icon, player2Icon))
                alph = max(value, alph)
                if(alph >= beta):
                    break
            return value
        else:
            value = 9000
            for i in range(7):
                board =  Board(gBorde) 
                board.addPiece(i,player1Icon)
                board.showBord(player1Icon,player1Icon)
                value = min(value, self.minMax(board.gameBord, depth-1, alph, beta, True, player1Icon, player2Icon))
                alph = min(value, alph)
                if(alph >= beta):
                    break
            return value
