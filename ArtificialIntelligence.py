from Board import *
import math
class ArtificialIntelligence():
    def __init__(self):
        self.EVALUATIONTABLE = []
        self.EVALUATIONTABLE.append([3, 4, 5, 7, 5, 4, 3])
        self.EVALUATIONTABLE.append([4, 6, 8, 10, 8, 6, 4])
        self.EVALUATIONTABLE.append([5, 8, 11, 13, 11, 8, 5])
        self.EVALUATIONTABLE.append([5, 8, 11, 13, 11, 8, 5])
        self.EVALUATIONTABLE.append([4, 6, 8, 10, 8, 6, 4])
        self.EVALUATIONTABLE.append([3, 4, 5, 7, 5, 4, 3])
    
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
            return self.evaluateContent(gBorde, player1Icon, player2Icon)
        if(maximazingPlayer):
            value = -9000
            for i in range(7):
                board =  Board(gBorde) 
                board.addPiece(i,player1Icon)
                value = max(value, self.minMax(board.gameBord, depth-1, alph, beta, False, player1Icon, player2Icon))
                alph = max(value, alph)
                if(alph >= beta):
                    break
            return value
        else:
            value = 9000
            for i in range(7):
                board =  Board(gBorde) 
                board.addPiece(i,player2Icon)
                value = max(value, self.minMax(board.gameBord, depth-1, alph, beta, True, player1Icon, player2Icon))
                alph = max(value, alph)
                if(alph >= beta):
                    break
            return value
