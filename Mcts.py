'''
Written by: Christopher Yong
'''

import numpy as np
import sys
import copy
import time
import random
from Board import *


# the following code was adapted and modified from: http://mcts.ai/code/python.html
##################################################


class Node:
    def __init__(self, move=None, parent=None, state=None, board=None):

        self.state = state
        boardcp = Board(board.gameBord, board.getTurn())
        self.parent = parent
        self.move = move
        self.untriedMoves = board.getMoves(boardcp)
        self.childNodes = []
        self.wins = 0
        self.visits = 0
        self.player = Board.getTurn(boardcp)

    def selection(self):
        # return child with largest UCT value
        foo = lambda x: x.wins / x.visits + np.sqrt(2 * np.log(self.visits) / x.visits)
        return sorted(self.childNodes, key=foo)[-1]

    def expand(self, move, state,board):
        # return child when move is taken
        # remove move from current node
        boardcp = Board(board.gameBord, board.getTurn())
        child = Node(move=move, parent=self, state=state, board=boardcp)
        self.untriedMoves.remove(move)
        self.childNodes.append(child)
        return child

    def update(self, result):
        if(result == 2):
            self.wins += 1
        elif(result ==0 ):
            self.wins += 0.5
        self.visits += 1

def MCTS(currentState, itermax, player1Icon, player2Icon, currentNode=None, timeout=100, board=None):
    rootnode = Node(state=currentState, board =Board())
    if currentNode is not None: rootnode = currentNode

    start = time.clock()
    for i in range(itermax):
        node = rootnode

        boardcp=Board(board.gameBord, board.getTurn())

        # selection
        # keep going down the tree based on best UCT values until terminal or unexpanded node
        while node.untriedMoves == [] and node.childNodes != []:
            node = node.selection()
            boardcp.addPieceSumulation(node.move, player1Icon, player2Icon)

        # expand
        if node.untriedMoves != []:
            m = random.choice(node.untriedMoves)
            state = None

            boardcp.addPieceSumulation(m, player1Icon, player2Icon,)
            node = node.expand(m, state,boardcp)

        # rollout
        while boardcp.getMoves(boardcp):
            boardcp.addPieceSumulation(random.choice(boardcp.getMoves(boardcp)), player1Icon, player2Icon)

        # backpropagate
        while node is not None:

            node.update(boardcp.chekFinal(player1Icon, player2Icon))
            node = node.parent

        duration = time.clock() - start
        if duration > timeout: break

    foo = lambda x: x.wins / x.visits
    sortedChildNodes = sorted(rootnode.childNodes, key=foo)[::-1]
    print("AI\'s computed winning percentages")
    for node in sortedChildNodes:
        print('Move: %s    Win Rate: %.2f%%' % (node.move + 1, 100 * node.wins / node.visits))
    print('Simulations performed: %s\n' % i)
    return rootnode, sortedChildNodes[0].move


######################################################
