from ArtificialIntelligence import *
from Board import *
from Player import *
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
        #aI.updateEvaluation(row,col,player1.playerAI)
        if (board.chekWin(player1.playerIcon)):
            print("PLAYER 1 GANHOU")
            board.showBord(player1.playerIcon, player2.playerIcon)
            break
        board.showBord(player1.playerIcon, player2.playerIcon)

        aiCol = aI.getNextPosition(board,7,player1.playerIcon,player2.playerIcon)
        piece = board.addPiece(aiCol,player2.playerIcon)
        row = piece
        #aI.updateEvaluation(row,aiCol, player2.playerAI)
        if (board.chekWin(player2.playerIcon)):
            print("PLAYER 2 GANHOU")
            board.showBord(player1.playerIcon, player2.playerIcon)
            break
        board.showBord(player1.playerIcon, player2.playerIcon)
        
        '''iaCol = aI.getNextPosition(board,player1.playerIcon,player2.playerIcon)
        for col in range(7):
            gBoard = Board(board.gameBord)
            gBoard.addPiece(col,player2.playerIcon)
            if (gBoard.chekWin(player2.playerIcon)):
                socre[col] = 1000000
                continue
            socre[col] =  aI.minMax(gBoard.gameBord , 7, -9000, 9000, True, player1.playerIcon, player2.playerIcon)
        print(socre)
        row = board.addPiece(getMin(socre),player2.playerIcon)
        #aI.updateEvaluation(row,getMin(socre),player2.playerAI)
        if(board.chekWin(player2.playerIcon)):
            print("PLAYER 2 GANHOU")
            board.showBord(player1.playerIcon, player2.playerIcon)
            break'''
    return 0

main()

