
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
        elif(result ==0 ):
            self.wins += 0.5
        elif(result == 1):
            self.loss += 1
            if(self.wins>0):
                self.wins -= 1
        self.visits += 1

def MCTS(currentState, itermax, player1Icon, player2Icon, currentNode=None, timeout=100, board=None):
    rootnode = Node(state=currentState, board =Board(currentState.gameBoard, currentState.turn))
    if currentNode is not None: rootnode = currentNode
    currentState.showBord(player1Icon,player2Icon)
    start = time.clock()
    for i in range(itermax):
        node = rootnode
        boardcp=Board(board.gameBoard, board.getTurn())

        while node.untriedMoves == [] and node.childNodes != []:
            node = node.selection()
            print("turno antes inserir  1 ---->",boardcp.getTurn())
            boardcp.addPieceSumulation(node.move, player1Icon, player2Icon)
            boardcp.showBord(player1Icon,player2Icon)
            print("turno depois inserir 1 ---->",boardcp.getTurn())
            

        if node.untriedMoves != []:
            m = random.choice(node.untriedMoves)
            state = None
            print("turno antes inserir  2 ---->",boardcp.getTurn())
            boardcp.addPieceSumulation(m, player1Icon, player2Icon)
            boardcp.showBord(player1Icon,player2Icon)
            print("turno depois inserir 2 ---->",boardcp.getTurn())
            node = node.expand(m, state,boardcp)

        while boardcp.getMoves(boardcp):
            print("turno antes inserir  3 ---->",boardcp.getTurn())
            boardcp.addPieceSumulation(random.choice(boardcp.getMoves(boardcp)), player1Icon, player2Icon)
            boardcp.showBord(player1Icon,player2Icon)
            print("turno depois inserir 3 ---->",boardcp.getTurn())
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
    print("AI\'s computed winning percentages")
    for node in sortedChildNodes:
        print('Move: %s   Win Rate: %.2f%%' % (node.move , 100 * node.wins / node.visits))
        print('Move: %s   Loss Rate: %.2f%%' % (node.move , 100 * node.loss / node.visits))
    print('Simulations performed: %s\n' % i)
    print("enviando ---------->",sortedChildNodes[0])
    print("enviando ---------->",sortedChildNodes[0].move)
    return rootnode, sortedChildNodes[0].move

