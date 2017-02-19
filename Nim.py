'''
Created on Feb 11, 2017

@author: will
'''

import actionTree, random

class SimpleNim(actionTree.gameRules):
    #a board is just an integer
    #a trun is removing 1, 2 or 3 from the value
    #win by reducing the value to 0
    
    def validMoves(self, board):
        if board>=3:
            return [1,2,3]
        elif board==2:
            return [1,2]
        elif board==1:
            return [1]
        else:
            return []
    
    def isValidMove(self, board, move):
        return board>=move
    
    def isLoss(self, board):
        return board==0
    
    def makeMove(self, board, move, hypothetical=True):
        if not hypothetical:
            print(str(move)+" were removed")
            for player in self.players:
                player.moveMade(move)
        return board-move
    
game=SimpleNim()

class nimTree(actionTree.actionTree):
    actionTree.actionTree.theGame=game
    
    def subNode(self,move):
        #probably could use a class variable referencing  the class instead
        return nimTree(self,actionTree.actionTree.theGame.makeMove(self.board,move),move)

    def holistic(self):
        self.changeScore(0.2)

board=20
head=nimTree(None,board,None)
p1=actionTree.ai(head,300)
#p2=actionTree.ai(head,30)
game.setPlayers([p1])#p2 removed for debugging
while board>0:
    p1.eval()
    print(str(board))
    print("p1", end=": ")
    board=game.makeMove(board,p1.chooseMove(),False)
    if board>0:
        #p2.eval()
        print(str(board))
        #print("p2", end=": ")
        #board=game.makeMove(board,p2.chooseMove(),False)
        board=game.makeMove(board,int(input("Your turn")),False)
print(board)
    
    