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
    aI = ArtificialIntelligence()
    gameing = True
    player1 = Player("1",False)
    player2 = Player("2",True)
    choiceAi = 0
    while ((choiceAi!=1)and (choiceAi!=2)): 
        print("Escola o modo de jogo:")
        print("(1) Humano x IA MinMax Alpha Beta")
        print("(2) Humano x IA MCTS")
        choiceAi =int(input("Digite o modo desejado: "))
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
        row = piece
        col = playerInput
        if (board.chekWin(player1.playerIcon)):
            print("PLAYER 1 GANHOU")
            board.showBord(player1.playerIcon, player2.playerIcon)
            break
        board.showBord(player1.playerIcon, player2.playerIcon)
        if(choiceAi == 1):
            aiCol = aI.getNextPosition(board,5,player1.playerIcon,player2.playerIcon)
        else:
            node = Node(state=board, board = board)
            node, aiCol = MCTS(board, 100000, player1.playerIcon, player2.playerIcon, currentNode=node, timeout=2, board = board)
        piece = board.addPiece(aiCol,player2.playerIcon)
        if (board.chekWin(player2.playerIcon)):
            print("PLAYER 2 GANHOU")
            board.showBord(player1.playerIcon, player2.playerIcon)
            break
    return 0

main()

