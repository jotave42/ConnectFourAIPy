from ArtificialIntelligence import *
from Board import *
from Player import *
from Mcts import *
import random

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
    choiceAi = 0
    val = random.randint(1,2)
    while ((choiceAi!=1)and (choiceAi!=2) and (choiceAi!=3)): 
        print("Escola o modo de jogo:")
        print("(1) Humano x IA MinMax Alpha Beta")
        print("(2) Humano x IA MCTS")
        print("(3) IA MCTS x IA MinMax Alpha Beta")
        print(val,"vall")
        choiceAi =int(input("Digite o modo desejado: "))
    while(True):
        piece = -1

        if(choiceAi == 3):
            if (val == 1):

                print("======================MINMAX====================")
                aiCol = aI.getNextPosition(board, 5, player1.playerIcon, player2.playerIcon)
                piece = board.addPiece(aiCol, player2.playerIcon)
                if (board.chekWin(player2.playerIcon)):
                    print("PLAYER MINMAX GANHOU")
                    board.showBoard(player1.playerIcon, player2.playerIcon)
                    break
                board.showBoard(player1.playerIcon, player2.playerIcon)
                print("=====================MCTS=======================")
                node = Node(state=board, board=board)
                node, aiCol = MCTS(board, 1000000, player2.playerIcon, player1.playerIcon, curNode=node, timeBrk=10,board=board)
                piece = board.addPiece(aiCol, player1.playerIcon)
                if (board.chekWin(player1.playerIcon)):
                    print("PLAYER MCTS GANHOU")
                    board.showBoard(player1.playerIcon, player2.playerIcon)
                    break
                board.showBoard(player1.playerIcon, player2.playerIcon)
            elif (val == 2):
                print("=====================MCTS=======================")
                node = Node(state=board, board=board)
                node, aiCol = MCTS(board, 1000000, player1.playerIcon, player2.playerIcon, curNode=node, timeBrk=10, board=board)
                piece = board.addPiece(aiCol, player2.playerIcon)
                if (board.chekWin(player2.playerIcon)):
                    print("PLAYER MCTS GANHOU")
                    board.showBoard(player1.playerIcon, player2.playerIcon)
                    break
                board.showBoard(player1.playerIcon, player2.playerIcon)
                print("======================MINMAX====================")
                aiCol = aI.getNextPosition(board, 5, player2.playerIcon, player1.playerIcon)
                piece = board.addPiece(aiCol, player1.playerIcon)
                if (board.chekWin(player1.playerIcon)):
                    print("PLAYER MINMAX GANHOU")
                    board.showBoard(player1.playerIcon, player2.playerIcon)
                    break
                board.showBoard(player1.playerIcon, player2.playerIcon)

        else:
            while(piece<0):
                print("Estado Atual do Tabuleiro: ")
                board.showBoard(player1.playerIcon, player2.playerIcon)
                playerInput = int (input("Digite a coluna: "))
                piece = board.addPiece(playerInput,player1.playerIcon)
                if(piece < 0):
                    print("POSICAO INVALIDA")
            row = piece
            col = playerInput
            if (board.chekWin(player1.playerIcon)):
                print("PLAYER 1 GANHOU")
                board.showBoard(player1.playerIcon, player2.playerIcon)
                break
            board.showBoard(player1.playerIcon, player2.playerIcon)
            if(choiceAi == 1):
                aiCol = aI.getNextPosition(board,5,player1.playerIcon,player2.playerIcon)
            else:
                node = Node(state=board, board = board)
                node, aiCol = MCTS(board, 5000000, player1.playerIcon, player2.playerIcon, curNode=node, timeBrk=10, board = board)
            piece = board.addPiece(aiCol,player2.playerIcon)
            if (board.chekWin(player2.playerIcon)):
                print("PLAYER 2 GANHOU")
                board.showBoard(player1.playerIcon, player2.playerIcon)
                break
    return 0

main()

