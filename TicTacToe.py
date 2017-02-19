import actionTree as ai
import grid

class ticTacToe(ai.gameRules):
    #board should be a grid object and also have a player turn stored
    
    def validMoves(self, board):
        moves=[]
        for x in range(board.width):
            for y in range(board.height):
                if board.acess(x,y)=="":
                    moves.append((x,y))
        return moves
    
    def isLoss(self, board):#replace with is win which also takes the move as an argument
        symbol=board.player.symbol
        for x in range(board.width):#checks vertical lines
            line=True
            for y in range(board.height):
                if board.acess(x,y).info==symbol or board.acess().info=="":
                    line=False
            if line:
                return True
        for y in range(board.height):#checks horizontal lines
            line=True
            for x in range(board.width):
                if board.acess(x,y)==symbol or board.acess()=="":
                    line=False
            if line:
                return True
        #checks both diagonals
        line=True
        for a in range(board.height):
            if board.acess(a,a)==symbol or board.acess()=="":
                    line=False
            if line:
                return True
        line=True
        for a in range(board.height):
            if board.acess(a,2-a)==symbol or board.acess()=="":
                    line=False
            if line:
                return True
        return False
                
    
    def isDraw(self, board):
        for x in range(board.width):
            for y in range(board.height):
                if board.acess(x,y).info:
                    return False
        return True

class gameStateTTT:#should inherit from a general gameState
    def __init__(self,grid,player):
        self.grid=grid
        self.player=player
        
    def acess(self,x,y):
        return self.grid.acess().info
        
    #should define hash and eq
    
        
    
        