from ArtificialIntelligence import *
from Board import *
from Player import *
from Mcts import *
def getMin(numbers):
    minValue = numbers[0]
    pos = 0
    for i in range(len(numbers)):
        if(minValue > numbers[i]):
            minValue = numbers[i]
            pos = i
        return pos

def main():
    board = Board()
    node = Node(state=board, board = board)
    aI = ArtificialIntelligence()
    gameing = True
    player1 = Player("1",False)
    player2 = Player("2",True)
    while(True):
        piece = -1
        socre =[0]*7
        while(piece<0):
            print("Estado Atual do Tabuleiro: ")
            board.showBord(player1.playerIcon, player2.playerIcon)
            playerInput = int (input("Digite a coluna: "))
            print("turn befor add-->",board.getTurn())
            piece = board.addPiece(playerInput,player1.playerIcon)
            print("turn AFTER add-->",board.getTurn())
            if(piece < 0):
                print("POSICAO INVALIDA")
        row = piece
        col = playerInput
        if (board.chekWin(player1.playerIcon)):
            print("PLAYER 1 GANHOU")
            board.showBord(player1.playerIcon, player2.playerIcon)
            break
        board.showBord(player1.playerIcon, player2.playerIcon)
        #aiCol = aI.getNextPosition(board,7,player1.playerIcon,player2.playerIcon)

        node, col = MCTS(board, 20000, player1.playerIcon, player2.playerIcon, currentNode=node, timeout=2, board = board)
        print(col , "coluuuuuuunnnnnaaaa")
        piece = board.addPiece(col,player2.playerIcon)
        row = piece
        if (board.chekWin(player2.playerIcon)):
            print("PLAYER 2 GANHOU")
            board.showBord(player1.playerIcon, player2.playerIcon)
            break
        board.showBord(player1.playerIcon, player2.playerIcon)
        
    return 0

main()

