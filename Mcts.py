from Board import *
import time

class Mcts:
    def __init__(self, time):
        self.width = Board.width
        self.time = time
        self.root = MctsNode(None,self.board);

    def update(self,move):
        if(self.root.children[move] != None):
            self.root = self.root.children[move]
        else:
            self.root = MctsNode(None,self.root.board.addable(move))

    def getOptimalMove(self):
        stop = time.clock_gettime_ns() + self.time
        par = time.clock_gettime_ns()
        while(stop > par):
            self.selectNode = MctsNode.select
            if(self.selectNode == None):
                self.expandedNode = MctsNode.simulate(self.selectNode)
                self.result = MctsNode.simulate(self.expandedNode)
                MctsNode.backPropagate(self.expandedNode,self.result)
            par = time.clock_gettime_ns()
        maxIndex = -1

        for i in range (0,Board.width,1):
            if(self.root.children[i] != None):
                if maxIndex == -1 or self.root.children[i].visits > self.root.children[maxIndex].visits:
                    maxIndex = i

        return maxIndex

    def select(self):
        return self.select(self.root)

    def select(self, parent):

        for i in range(0,Board.width,1):
            if(parent.children[i] == None and parent.board.addable(i)):
                return parent

        maxSelectionVal = -1
        maxindex = -1
        for i in range(0, Board.width, 1):
            if(not parent.board.addable(i)):
                continue
            curremtChild = parent.children[i]
            if(parent.board.addPiece())



class MctsNode:

    def __init__(self,parent,board):
        self.parent = parent
        self.board = board
        self.visits = 0
        self.playerWins = 0
        self.children = []

    def incrementVisit(self):
        self.visits += 1
        return self.visits

    def incrementPLayerWins(self, result):
         self.playerWins += 1
         return self.playerWins



