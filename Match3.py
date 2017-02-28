import grid, random

def print_grid(grid_to_print,h,w):
    "displays a grid with row and column numbers"
    print("\t",end='|')
    for k in range(w):
        print("  ",str(k+1),end='\t|')
    print("")
    for k in range(w):
        print("__________",end="")
    print('')
    for y in range(h):
        x=0
        print("  ",y+1,end='\t|')
        for x in range(w):
            print(grid_to_print.acess(x,y).info,end="\t|")
        print("")
        for x in range(w):
            print("__________",end="")
        print('')

def check_matches(gamegrid,x,y,squeres,original=False):
    me=gamegrid.acess(x,y)
    squeres.append(me)
    neibours=me.neibours()
    minfo=me.info
    for squere in neibours:
        if squere !="":
            if squere.info == me.info != "" and squere not in squeres:
                squeres=check_matches(gamegrid,squere.x,squere.y,squeres)
    if len(squeres)>=3 and original:
        for squere in squeres:
            if squere!="":
                squere.change("")
        upgrade(x,y,gamegrid,minfo)
    else:
        return squeres

def upgrade(x,y,gamegrid,current):
    ITEMS=(",,,","@%@","q^p","/\\","|^|^|","|^|#|^|",":)","gold","+++","")
    up=""
    counter=0
    for j in ITEMS:
        counter+=1
        if j==current:
            up=ITEMS[counter]
            place(up,gamegrid,x,y)

def ask(item,gamegrid):
    try:
        x=int("0"+input("in which coulumn do you want to place a "+item+":"))-1
        y=int("0"+input("in which row do you want to place "+item+":"))-1
    except ValueError:
            print("unusable symbol")
            ask(item,gamegrid)
    else:
        if gamegrid.acess(x,y)=="":
            print("unusable coordonates")
            ask(item,gamegrid)
        elif gamegrid.acess(x,y).info=="":
            place(item,gamegrid,x,y)
        else:
            print("squere is full")
            ask(item,gamegrid)
    
def place(item,gamegrid,x,y):
    gamegrid.change(item,x,y)
    a=check_matches(gamegrid,x,y,[],True)


def main():
    w=6#width
    h=6#hight
    gamegrid=grid.grid(h,w)
    gamegrid.change_all("")
    luck=0
    choice=""
    while choice!="quit":
        print_grid(gamegrid,h,w)
        l=luck+random.randint(-4,7)
        if l>=10:
            item="/\\"
            luck-=12
        elif l>=6:
            item="q^p"
            luck-=5
        elif l>=3:
            item="@%@"
            luck-=2
        else:
            item=",,,"
            luck+=1
        ask(item,gamegrid)
        choice=input("type quit to quit or anything else to continue")#consider removing


main()
