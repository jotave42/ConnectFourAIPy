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
        self.untriedMoves = board.getMoves(self.boardcp)
        self.childNodes = []
        self.wins = 0
        self.loss = 0
        self.visits = 0
        self.player = Board.getTurn(self.boardcp)

    def selection(self):

        foo = lambda x: x.wins / x.visits + 9000000*np.sqrt(2 * np.log(self.visits) / x.visits)
        foo2 = lambda x: x.loss / x.visits + 9000000*np.sqrt(2 * np.log(self.visits) / x.visits)
        foo3 = lambda x : (foo(x),foo2(x))
        return sorted(self.childNodes, key=foo3)[-1]

    def expand(self, move, state,board):

        boardcp = Board(board.gameBoard, board.getTurn())
        child = Node(move=move, parent=self, state=state, board=boardcp)
        self.untriedMoves.remove(move)
        self.childNodes.append(child)
        return child

    def update(self, result):
        if(result == 2):
            self.wins += 1
            if(self.loss>1):
                self.loss-=1
        elif(result ==0 ):
            self.wins += 0.5
            if(self.loss>0.5):
                self.loss-=0.5
        elif(result == 1):
            self.loss += 1
            if(self.wins>1):
                self.wins -= 1
        self.visits += 1

def MCTS(currentState, itermax, player1Icon, player2Icon, currentNode=None, timeout=100, board=None):
    rootnode = Node(state=currentState, board =Board(currentState.gameBoard, currentState.turn))
    if currentNode is not None: rootnode = currentNode
    start = time.clock()
    for i in range(itermax):
        node = rootnode
        boardcp=Board(board.gameBoard, board.getTurn())

        while node.untriedMoves == [] and node.childNodes != []:
            node = node.selection()
            boardcp.addPieceSumulation(node.move, player1Icon, player2Icon)
        if node.untriedMoves != []:
            m = random.choice(node.untriedMoves)
            state = None
            boardcp.addPieceSumulation(m, player1Icon, player2Icon)
            node = node.expand(m, state,boardcp)

        while boardcp.getMoves(boardcp):
            boardcp.addPieceSumulation(random.choice(boardcp.getMoves(boardcp)), player1Icon, player2Icon)
            if(boardcp.chekFinal(player1Icon,player2Icon)>-1):
                break

        while node is not None:
            node.update(boardcp.chekFinal(player1Icon, player2Icon))
            node = node.parent

        duration = time.clock() - start
        if duration > timeout: break

    foo =  lambda x: x.wins / x.visits
    foo2 = lambda x: x.loss / x.visits
    foo3 = lambda x : (foo(x),foo2(x))
    sortedChildNodes = sorted(rootnode.childNodes, key=foo3)[::-1]
#    print("AI\'s computed winning percentages")
#    for node in sortedChildNodes:
#        print('Move: %s   Win Rate: %.2f%%' % (node.move , 100 * node.wins / node.visits))
#        print('Move: %s   Loss Rate: %.2f%%' % (node.move , 100 * node.loss / node.visits))
    return rootnode, sortedChildNodes[0].move

