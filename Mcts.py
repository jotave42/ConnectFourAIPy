import numpy as np
import time
import random
from Board import *

class Node:
    def __init__(self, move=None, parent=None, state=None, board=None):
        self.boardcp = Board(board.gameBoard, board.getTurn())
        self.state = self.boardcp
        self.parent = parent
        self.move = move
        self.notVisitedMoves = board.getMoves(self.boardcp)
        self.childNodes = []
        self.wins = 0
        self.loss = 0
        self.visits = 0
        self.player = Board.getTurn(self.boardcp)



    def expand(self, move, state,board):

        boardcp = Board(board.gameBoard, board.getTurn())
        child = Node(move=move, parent=self, state=state, board=boardcp)
        self.notVisitedMoves.remove(move)
        self.childNodes.append(child)
        return child

    def update(self, res):
        if(res == 2):
            self.wins += 1
            if(self.loss>1):
                self.loss-=1
        elif(res == 0):
            self.wins += 0.5
            if(self.loss>0.5):
                self.loss-=0.5
        elif(res == 1):
            self.loss += 1
            if(self.wins>1):
                self.wins -= 1
        self.visits += 1


    def select(self):

        foo = lambda x: x.wins / x.visits + 100*np.sqrt(2 * np.log(self.visits) / x.visits)
        foo2 = lambda x: x.loss / x.visits + 100*np.sqrt(2 * np.log(self.visits) / x.visits)
        foo3 = lambda x : (foo(x),foo2(x))
        return sorted(self.childNodes, key=foo3)[-1]

def MCTS(curState, maxIteration, player1Icon, player2Icon, curNode=None, timeBrk=100, board=None):
    rtnode = Node(state=curState, board =Board(curState.gameBoard, curState.turn))
    if curNode != None: rtnode = curNode
    start = time.clock()
    for i in range(maxIteration):
        node = rtnode
        boardcp=Board(board.gameBoard, board.getTurn())

        while node.notVisitedMoves == [] and node.childNodes != []:
            node = node.select()
            boardcp.addPieceSimulation(node.move, player1Icon, player2Icon)
        if node.notVisitedMoves != []:
            m = random.choice(node.notVisitedMoves)
            state = None
            boardcp.addPieceSimulation(m, player1Icon, player2Icon)
            node = node.expand(m, state,boardcp)

        while boardcp.getMoves(boardcp):
            boardcp.addPieceSimulation(random.choice(boardcp.getMoves(boardcp)), player1Icon, player2Icon)
            if(boardcp.chekFinal(player1Icon,player2Icon)>-1):
                break

        while node != None:
            node.update(boardcp.chekFinal(player1Icon, player2Icon))
            node = node.parent

        timeStp = time.clock() - start
        if timeStp > timeBrk: break

    foo =  lambda x: x.wins / x.visits
    foo2 = lambda x: x.loss / x.visits
    foo3 = lambda x : (foo(x),foo2(x))
    childSort = sorted(rtnode.childNodes, key=foo3)[::-1]
    return rtnode, childSort[0].move

