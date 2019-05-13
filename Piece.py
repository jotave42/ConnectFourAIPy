class Piece:
    evaluate = 0
    row = 0
    col = 0
    def __init__(self, evaluate, row, col):
        self.evaluate = evaluate
        self.row = row
        self.col = col