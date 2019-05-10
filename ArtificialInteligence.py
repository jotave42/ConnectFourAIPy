from Board import *
import math
class ArtificialIntelligence:
    def __init__(self):
        self.EVALUATIONTABLE = []
        self.EVALUATIONTABLE.append([3, 4, 5, 7, 5, 4, 3],
                                    [4, 6, 8, 10, 8, 6, 4],
                                    [5, 8, 11, 13, 11, 8, 5],
                                    [5, 8, 11, 13, 11, 8, 5],
                                    [4, 6, 8, 10, 8, 6, 4],
                                    [3, 4, 5, 7, 5, 4, 3])
    
    def evaluateContent(gBorde, player1Icon, player2Icon):
        utility = 138
        summ = 0
        for row  in range(6):
            for colum in range(7):
                if(gBorde[row][colum] == player1Icon ):
                    summ -= EVALUATIONTABLE[row][colum]
                elif(gBorde[row][colum] == player2Icon ):
                    summ += EVALUATIONTABLE[row][colum]
        return utility + summ

    def minMax(self, gBorde, depth, alph, beta, maximazingPlayer, player1Icon, player2Icon):
        if(depth == 0):
            return self.evaluateContent(gBorde),
        if(maximazingPlayer):
            value = -3000
            for i in range(7):
               board =  Board(gBorde) 
               board.addPiece(i,player1Icon)
               value = max(value, minMax(gBorde, depth-1, alph, beta, False, player1Icon, player2Icon))
               alph = max(value, alph)
               if(alph >= beta):
                   break
            return value
        else:
            value = 3000
            for i in range(7):
               board =  Board(gBorde) 
               board.addPiece(i,player2Icon)
               value = max(value, minMax(gBorde, depth-1, alph, beta, False,player2Icon))
               alph = max(value, alph)
               if(alph >= beta):
                   break
            return value
