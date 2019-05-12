from Board import *
from Piece import *
import math

class ArtificialIntelligence:
    children =[]

    def getNextPosition(self,board,depth,player1Icon,player2Icon):
        
        bestOption = self.minMax2(board,depth,player1Icon,player2Icon,True)
        return bestOption

    def minMax2(self, board, depth, player1Icon,player2Icon ,maximazingPlayer): #player2 eh ia
        final = board.chekFinal(player1Icon,player2Icon)
        if(final != -1):
            if (final == 0):
                return 0 #checar no futuro se zero eh sufuciente para  o empate
            if (final == 1):
                return -1000000
            if  (final == 2):
                return 1000000
        elif(depth == 0):
                return board.evaluateContent(player1Icon,player2Icon)
        return 0
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
                board.addPiece(i,player2Icon)
                board.showBord(player1Icon,player2Icon)
                value = min(value, self.minMax(board.gameBord, depth-1, alph, beta, True, player1Icon, player2Icon))
                beta = min(value, beta)
                if(alph >= beta):
                    break
            return value
    
    
    def setChildrens(self,gameBord,playerIcon):
        self.children=[]
        for col in range(len(gameBord[0])):
            row = len(gameBord) -1
            while((gameBord[row][col] != 0) and (row>=0)):
                row -=1
            if(row<6):
                newChildren = Board(gameBord)
                newChildren.addPiece(col,playerIcon)
                self.children.append(newChildren)
        return self.children