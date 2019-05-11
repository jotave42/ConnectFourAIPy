from Board import *

class Mcts:
    def __init__(self, time):
        self.width = Board.width
        self.time = time
        root = Mcts.MctsNode(None,self.board);

    def update(self,move):
        if(self.root)

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



