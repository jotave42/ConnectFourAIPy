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
            piece = board.addPiece(playerInput,player1.playerIcon)
            if(piece < 0):
                print("POSICAO INVALIDA")
        board.showBord(player1.playerIcon, player2.playerIcon)
        if (board.chekWin(player1.playerIcon)):
            print("PLAYER 1 GANHOU")
            board.showBord(player1.playerIcon, player2.playerIcon)
            break
        for col in range(7):
            gBoard = Board(board.gameBord)
            gBoard.addPiece(col,player2.playerIcon)
            if (gBoard.chekWin(player2.playerIcon)):
                socre[col] = 1000000
                continue
            socre[col] =  aI.minMax(gBoard.gameBord , 9, -9000, 9000, True, player1.playerIcon, player2.playerIcon)
        board.addPiece(getMin(socre),player2.playerIcon)
        if(board.chekWin(player2.playerIcon)):
            print("PLAYER 2 GANHOU")
            board.showBord(player1.playerIcon, player2.playerIcon)
            break
    return 0

main()

