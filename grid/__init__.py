class GridError(Exception):
    '''base error for grid module'''
    pass

class NotInGrid(GridError):
    def __init__(self, grid, coord):
        self.coord=coord
        self.grid=grid
        
    def __str__(self):
        return ('the coordinates:' + str(self.coord) + 'is not in grid')
    

class grid(object):
    '''a square based grid'''
    def __init__(self,height=6,width=6):
        self.main={}
        self.height=height
        self.width=width
        for x in range(width):
            for y in range(height):
                s=square(self,x,y)
                self.main[x,y]=s
    
    def clone(self):
        newGrid=grid(self.height, self.width)
        for x in range(newGrid.width):
            for y in range(newGrid.height):
                newGrid.change(self.acess(x,y).info,x,y)
        return newGrid
    
    def acess(self,x,y):
        '''returns the squere object at the given coordinates'''
        l=(x,y)
        if l in self.main.keys():
            return self.main[l]
        else:
            raise NotInGrid(self,l)

    def in_grid (self,x,y):
        if (x,y) in self.main:
            return True
        else:
            return False

    def change(self,new,x,y):
        '''edits the info of a squere item'''
        self.acess(x,y).change(new)

    def change_all(self,new=''):
        '''sets the info of all squeres in the grid to the new string''' 
        for xy in self.main.keys():
            x=xy[0]
            y=xy[1]
            self.change(new,x,y)

    def __str__(self):

        r=''
        for x in range(self.width):
            s=''
            for y in range(self.height):
                s= s+str(self.acess(x,y).info)
            r= r+s+'\n'
        return r
        
    def print_grid(self):
        "displays a grid with row and column numbers"
        print("\t", end="|")
        for k in range(self.width):
            print("  ",str(k+1),end='\t|')
        print("")
        for k in range(self.width+1):
            print("- - - -",end="\t")
        print('-')
        for y in range(self.height):
            x=0
            print('  ',y+1,end='\t|')
            for x in range(self.width):
                if self.acess(x,y).info==0:
                    print("",end="\t|")
                elif self.acess(x,y).info==1:
                    print("  X",end="\t|")
                elif self.acess(x,y).info==2:
                    print("  O",end="\t|")
                else:
                    print("ERROR",end="\t|")
            print('')
            for x in range(self.width+1):
                print("- - - -",end="\t")
            print('-')
        
class square(object):
    '''a squere in a grid'''
    def __init__(self,grid,x,y,info=''):
        self.grid=grid
        self.x=x
        self.y=y
        self.info=info

    def __str__(self):
        return "x:"+str(self.x)+" y:" +str(self.y)+"\ninfo:"+str(self.info)

    def change(self,new):
        self.info=new

    def neibours(self,diagonals=False,):
        reply=[]
        displace=[[-1,0],[1,0],[0,-1],[0,1]]
        if diagonals==True:displace=[[-1,0],[1,0],[0,-1],[0,1],[-1,-1],[1,-1],[-1,1],[1,1]]
        for disp in displace:
            if self.grid.in_grid(self.x+disp[0],self.y+disp[1]):
                reply.append(self.grid.acess(self.x+disp[0],self.y+disp[1]))
        '''reply.append(self.grid.acess(self.x+1,self.y))
        reply.append(self.grid.acess(self.x,self.y-1))
        reply.append(self.grid.acess(self.x,self.y+1))
        if diagonals==True:
            reply.append(self.grid.acess(self.x-1,self.y-1))
            reply.append(self.grid.acess(self.x-1,self.y+1))
            reply.append(self.grid.acess(self.x+1,self.y-1))
            reply.append(self.grid.acess(self.x+1,self.y+1))'''
        return reply