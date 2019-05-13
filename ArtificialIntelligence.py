from Board import *
import math

class ArtificialIntelligence:
    def heuristic(self, board,aiPlayerIcon,Player2Icon):
        heur = 0
        state = board.gameBoard
        for i in range(0, board.width):
            for j in range(0, board.height):
                # check horizontal streaks
                try:
                    # add player one streak scores to heur
                    if state[i][j] == state[i + 1][j] == aiPlayerIcon:
                        heur += 10
                    if state[i][j] == state[i + 1][j] == state[i + 2][j] == aiPlayerIcon:
                        heur += 100
                    if state[i][j] == state[i+1][j] == state[i+2][j] == state[i+3][j] == aiPlayerIcon:
                        heur += 10000

                    # subtract player two streak score to heur
                    if state[i][j] == state[i + 1][j] == Player2Icon:
                        heur -= 10
                    if state[i][j] == state[i + 1][j] == state[i + 2][j] == Player2Icon:
                        heur -= 100
                    if state[i][j] == state[i+1][j] == state[i+2][j] == state[i+3][j] == Player2Icon:
                        heur -= 10000
                except IndexError:
                    pass

                # check vertical streaks
                try:
                    # add player one vertical streaks to heur
                    if state[i][j] == state[i][j + 1] == aiPlayerIcon:
                        heur += 10
                    if state[i][j] == state[i][j + 1] == state[i][j + 2] == aiPlayerIcon:
                        heur += 100
                    if state[i][j] == state[i][j+1] == state[i][j+2] == state[i][j+3] == aiPlayerIcon:
                        heur += 10000

                    # subtract player two streaks from heur
                    if state[i][j] == state[i][j + 1] == Player2Icon:
                        heur -= 10
                    if state[i][j] == state[i][j + 1] == state[i][j + 2] == Player2Icon:
                        heur -= 100
                    if state[i][j] == state[i][j+1] == state[i][j+2] == state[i][j+3] == Player2Icon:
                        heur -= 10000
                except IndexError:
                    pass

                # check positive diagonal streaks
                try:
                    # add player one streaks to heur
                    if not j + 3 > board.height and state[i][j] == state[i + 1][j + 1] == aiPlayerIcon:
                        heur += 100
                    if not j + 3 > board.height and state[i][j] == state[i + 1][j + 1] == state[i + 2][j + 2] == aiPlayerIcon:
                        heur += 100
                    if not j + 3 > board.height and state[i][j] == state[i+1][j + 1] == state[i+2][j + 2] \
                            == state[i+3][j + 3] == aiPlayerIcon:
                        heur += 10000

                    # add player two streaks to heur
                    if not j + 3 > board.height and state[i][j] == state[i + 1][j + 1] == Player2Icon:
                        heur -= 100
                    if not j + 3 > board.height and state[i][j] == state[i + 1][j + 1] == state[i + 2][j + 2] == Player2Icon:
                        heur -= 100
                    if not j + 3 > board.height and state[i][j] == state[i+1][j + 1] == state[i+2][j + 2] \
                            == state[i+3][j + 3] == Player2Icon:
                        heur -= 10000
                except IndexError:
                    pass

                # check negative diagonal streaks
                try:
                    # add  player one streaks
                    if not j - 3 < 0 and state[i][j] == state[i+1][j - 1] == aiPlayerIcon:
                        heur += 10
                    if not j - 3 < 0 and state[i][j] == state[i+1][j - 1] == state[i+2][j - 2] == aiPlayerIcon:
                        heur += 100
                    if not j - 3 < 0 and state[i][j] == state[i+1][j - 1] == state[i+2][j - 2] \
                            == state[i+3][j - 3] == aiPlayerIcon:
                        heur += 10000

                    # subtract player two streaks
                    if not j - 3 < 0 and state[i][j] == state[i+1][j - 1] == Player2Icon:
                        heur -= 10
                    if not j - 3 < 0 and state[i][j] == state[i+1][j - 1] == state[i+2][j - 2] == Player2Icon:
                        heur -= 100
                    if not j - 3 < 0 and state[i][j] == state[i+1][j - 1] == state[i+2][j - 2] \
                            == state[i+3][j - 3] == Player2Icon:
                        heur -= 10000
                except IndexError:
                    pass
        return heur
    def getNextPosition(self,board,depth,player1Icon,player2Icon):
        value, bestOption = self.minMax2(board,depth,player1Icon,player2Icon,True,-math.inf, math.inf)
        return bestOption

    def minMax2(self, board, depth, player1Icon,player2Icon ,maximazingPlayer, alpha,beta): #player2 eh ia
        final = board.chekFinal(player1Icon,player2Icon)
        if(final != -1):
            if (final == 0):
                return 0,-1 #checar no futuro se zero eh sufuciente para  o empate
            if (final == 1):
                return -1000000,-1
            if  (final == 2):
                return 1000000,-1
        if(depth == 0):
                return self.heuristic(board,player1Icon,player2Icon),-1
        if(maximazingPlayer):
            value = -math.inf
            replace = lambda x: x > value
        else:
            value = math.inf
            replace = lambda x: x < value
        bestOption = -1
        minMaxChildrens = []
        minMaxChildrens = self.setChildrens(board,player1Icon,player2Icon)
        for child in minMaxChildrens:
            move, childBoard = child
            #childBoard.showBord(player1Icon,player2Icon)#comente esse linha para nao ver todos as jogadas simuladas
            nextPlay = self.minMax2(childBoard, depth-1,player1Icon,player2Icon, not maximazingPlayer, alpha, beta)[0]
            if replace(nextPlay):
                value = nextPlay
                bestOption = move
            if maximazingPlayer:
                alpha = max(alpha, nextPlay)
            else:
                beta = min(beta, nextPlay)
            if alpha >= beta:
                break
        return value, bestOption


    
    def setChildrens(self,board,player1Icon,player2Icon):
        childrens=[]
        gameBoard = board.gameBoard
        turno=board.getTurn()
        for col in range(board.width):
            row = board.height -1
            while((gameBoard[row][col] != 0) and (row>=0)):
                row -=1
            if(row>=0):
                newChildren = Board(gameBoard,board.getTurn())
                newChildren.addPieceSumulation(col,player1Icon,player2Icon)
                childrens.append((col,newChildren))
        return childrens