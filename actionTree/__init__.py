#the goal of this class is to create an Ai with an adjustable search pattern
#and holistic method for a game with arbitrary rules and two players

#features to add:
#quick-win, slow loss behaviour
#same position combination with game-state and node-dictionary
    #Reflectional/Rotational/player-swap symmetries (Game dependant)
#general cleanup, possibly transcribe to a faster language
#improve iteration distribution methods
#find a better option than the sub-node() method
#apply this to more games



class gameRules(object):
    
    def __init__(self):
        #represents the rules of the game, not the players or interface(s)
        pass
        
    def setPlayers(self,players):
        #added to prevent a cicular dependency
        #probably a bit messy
        self.players=players

    def validMoves(self,board):
        return []
        #should return an array of valid moves
    
    def isValidMove(self,board,move):
        pass
        #returns true or false
    
    def isWin(self,board):
        return False
        #returns true or false
    
    def isLoss(self,board):
        return False
        #returns true or false
    
    def isDraw(self,board):
        return False
        #returns true or false
    
    def isOver(self,board):#done
        if self.isWin(board):
            return True,1
        elif self.isLoss(board):
            return True,-1
        elif self.isDraw(board):
            return True, 0
        else:
            return False, 0
    
    def makeMove(self, board, move, hypothetical=True):
        #could check if move is valid first, but probably fits better elsewhere
        #returns the board with the given move
        pass

class actionTree:
    theGame=gameRules()
    
    #starting, ending, general, partially evaluated
    def __init__(self,previous,board,move):
        self.previous=previous
        self.score=0 #set to -1 for loss 1 for win, and between for a holistic
        #self.time=None #measures the number of moves before a guarenteed draw/win/loss. None if uncertain
        self.following=[] #length 0 means no following only when complete="Full"
        self.complete=False #false, Full, partial
        self.board=board
        self.move=move#move that gets to this position
        self.best=None#best action node available from here
        if previous==None or previous.player==1:
            self.player=0
        else:
            self.player=1
        
    def addFollowing(self):    
        #called by eval
        if self.following:
            return
        validMoves=actionTree.theGame.validMoves(self.board)
        for move in validMoves:
            self.following.append(self.subNode(move))
        #self.board=None #deactivated for debugging
        
    def subNode(self,move):
        #overwrite when updating class
        return actionTree(self,actionTree.theGame.makeMove(self.board,move),move)
    
    def holistic(self):
        #change this for different games
        value=0.1
        self.changeScore(value)
    
    def eval(self,iterations):#needs to update status and set board to None in some cases
        #returns number of unused iterations
        if iterations<=0: #negative iterations count as zero
            return iterations
        elif self.complete=="Full":#all endgames from here are visible, socore is not a holistic anymore
            return iterations
        elif self.complete=="Partial" : #has been evaluated but not to maximum depth
            self.distributeIters(iterations)
        else:#has not been evaluated at all
            a,b=actionTree.theGame.isOver(self.board)
            if a:
                self.changeScore(b)
                self.complete="Full"
                print("Endgame found")
                return iterations-1
            self.addFollowing()
            if iterations>len(self.following):#would have exited for game ended, must have following
                iterations=self.distributeIters(iterations)
                self.bestMove()
                self.complete="Partial"
                return iterations
            else:
                self.holistic()
                self.complete="Partial"
                return iterations-1; 
            
    def distributeIters(self,iterations):
        #must call eval of dependants with appropriate distributions
        #one of the tweakable parts of the ai (the other is the holistic)
        #must return unused iterations
        #must distribute at least one to each item in following
        for move in self.following:
            move.eval(iterations//len(self.following))
        return iterations%len(self.following)
        
    def bestMove(self):
        #sets score to that which creates the worst position for their opponent
        self.best=self.following[0]
        #probably a minimum/maximum method for this loop
        #low scores are prefered
        for node in self.following:#sets score to best case for opponent
            if node.score<self.best.score:
                self.best=node
            #add code using the time attribute
        self.changeScore(-(self.best.score))
        
    def changeScore(self,score):
        if self.score != score:
            self.score=score
            if self.previous:
                self.previous.bestMove()
   
class ai:#may inherit from player
    def __init__(self,node,standardIterations=50):
        self.head=node #represents current game state
        #creating two ais with the same head node is possible
        self.standardIterations=standardIterations
        
    def eval(self,iterations=None):
        if iterations==None:
            iterations=self.standardIterations
        iterations-=self.minEval()
        self.head.eval(iterations)

    def minEval(self):
        #might fit better in actionTree
        #provides the minimum number of iterations to avoid errors
        #may exceed minimum iterations for some cases
        #should be modified for games with many options per turn
        if self.head.complete:
            return 0        
        iterations=0
        if len(self.head.following)==0:
            self.head.addFollowing()
        for node in self.head.following:
            if not node.complete:
                node.eval(1)
                iterations+=1
        self.minEvalDone=True
        return iterations
                

    def moveMade(self,move):
        self.minEval()
        for node in self.head.following:
            if node.move==move:
                self.head=node
        #could add an else in case this move is missing
        #but that case should never occur
        
    def chooseMove(self):
        self.minEval()
        print("(",self.head.score, end=")")
        #ai will be informed that it's move was made and update head later
        return self.head.best.move
        
class gameState:
    #this is a placeholder stub
    def __init__(self,board,player):
        self.board=board
        self.player=player
    
    def __hash__(self):
        #define flipable lists
        #map (A,B,C,D,E) to ({A,B},{C,D},E)
        #hash is the minimum of the hash of the flippable list matrix
        #compared with the rotated positions hashed flipable list matrix
        pass
        
    
    def __eq__(self,other):
        return hash(self)==hash(other)
            
        
class game:
    #this is a placeholder stub
    def __init__(self,board,rules,players):
        self.board=board
        self.rules=rules
        self.players=players
        
    def play(self):
        player=self.players[0]
        gameOver=False
        while not gameOver:
            self.board=self.rules.makeMove(self.board,player.takeTurn(self.board),False)
            #should probably move the inform all players code to here
            #instead of having it in makeMove
            gameOver=self.rules.isOver(self.board)
            player=self.nextPlayer(player)
        #should add quit handling
    
    def quit(self):
        #should confirm that the player wants to quit and forfit/save and exit
        
    def nextPlayer(self,player):
        i=self.players.index(player)#not sure about method name
        if i==len(self.players):
            return self.players[0]
        else:
            return self.players[i+1]
        
        
class player:
    #this is a placeholder stub
    #human player and ai should be derived from this
    def __init__(self,name='player'):
        self.name=name
    
    def takeTurn(self,board):
        #should return a move,
        #gives ai time to think and 
        #activates the human player interface
        pass
    
class human(player):
    def __init__(self,name='player'):
        player.__init__(self, name)
        
    
    def takeTurn(self, board):
        player.takeTurn(self, board)
    