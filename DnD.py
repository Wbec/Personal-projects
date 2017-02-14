import random

def roll(number,sides=0):
    total=0
    reportCrit=False
    if number=='hit':
        number=1
        sides=20
        reportCrit=True
    if sides==0:
        sides=number
        number=1
    while number>0:
        total+=random.randint(1,sides)
        number-=1
    if reportCrit and total==20:
        print('CRITICAL!')
    return total

class player():
    playerList=[]

    def __init__(self,health,initiative,name='player'):
        player.playerList.append(self)
        self.name=name
        self.health=health
        self.initiative=initiative
        print(self)

    def __str__(self):
        return self.name+'\nHealth: '+str(self.health)+'\nInitative: '+str(self.initiative)+'\n'

    def play(self):
        print('It is now the turn of: '+str(self))
        i=input('type n for next or d for damage ')
        if i=='n':
            return 'next'
        elif i=='d':
            amount=int(input('how much: '))
            target=input('to who: ')
            print('\n')
            for m in monster.monsterList:
                if m.name==target:
                    m.d(amount)
            return 'next'
        
    def edit(self,h='same',i='same'):
        if h!='same': self.health=h
        if i!='same':self.initiative=i

    def d(self,amount):
        self.health-=amount
        print(self.name+'\nHealth: '+str(self.health))

class monster():
    monsterList=[]

    def __init__(self,name='blank'):
        self.name=name
        self.init2()
        self.health=self.maxHealth
        monster.monsterList.append(self)
        print(self)

    def __str__(self):
        return self.name+'\nHealth: '+str(self.health)+'\nInitative: '+str(int(self.initiative))+self.extraStr()+'\n'

    def init2(self):
        self.maxHealth=roll(1,7)+0
        self.initiative=roll(20)+0+random.random()-0.5

    def play(self):
        print('It is now the turn of: '+str(self))

    def d(self,amount):
        self.health-=amount
        print(self.name+'\nHealth: '+str(self.health)+'\n')
        if self.health<1:
            self.die()

    def die(self):
        global creatureOrder, playerNum
        print(self.name+' is dead\n')
        monster.monsterList.remove(self)
        creatureOrder.remove(self)
        playerNum-=1

    def edit(self,h='same',i='same'):
        if h!='same': self.health=h
        if i!='same':self.initiative=i

    def extraStr(self):
        return ''

    def turnstart(self):
        None

class dragon(monster):
    def init2(self):
        self.maxHealth=roll(4,8)+20
        self.initiative=roll(20)+3+random.random()-0.5
        self.name='Dragon'
        self.breath=True

    def play(self):
        print('It is now the turn of: '+str(self))
        prompt='Tpye a for basic attack, n for next'
        if self.breath:prompt+=', or b for breath'
        i=input(prompt)
        if i=='a':
            self.a()
            return 'next'
        elif i=='n':return'next'
        elif i=='b':
            if self.breath==True:
                self.breathAttack()
                return 'next'
            else:print('The dragon is breathless')
        
    def breathAttack(self):
        print('Fire Breath: '+str(roll('hit')+6)+'vs AC for ' +str(roll(3,8)+5)+'\n')
        self.breath=False
        

    def a(self):
        goodTarget=False
        target=input('to who: ')
        if target:
            for p in player.playerList:
                if p.name==target:
                    goodTarget=True
                    target=p
            if not goodTarget:print('invalid target')
        amount=roll(2,6)+2
        print('Slash: '+str(roll('hit')+5)+'vs AC for ' +str(amount))
        if goodTarget:
            if input('hit(y): ')=='y':
                target.d(amount)
        amount=roll(2,6)+2
        print('Slash: '+str(roll('hit')+5)+'vs AC for ' +str(amount))
        if goodTarget:
            if input('hit(y): ')=='y':
                target.d(amount)
        amount=str(roll(3,6)+5)
        print('Bite: '+str(roll('hit')+3)+'vs AC for ' +str(amount))
        if goodTarget:
            if input('hit(y): ')=='y':
                target.d(amount)
        print('\n')

    def extraStr(self):
        return '\nBreath: '+str(self.breath)

    def turnstart(self):
        if not self.breath:
            if roll(6)>4:
                self.breath=True
                print('Breath reset')


def order():
    creatures=monster.monsterList+player.playerList
    initiatives=[]
    ordered=[]
    for c in creatures:
        initiatives.append(c.initiative)
    initiatives.sort(reverse=True)
    for i in initiatives:
        for c in creatures:
            if c.initiative==i:
                ordered.append(c)
    print('**** Initiative order: ****\n')
    for i in ordered:
        print (i)
    print('**** End of initiative list ****\n')
    return ordered


def start():
    global currentPlayer, playerNum, creatureOrder
    creatureOrder=order()
    playerNum=len(creatureOrder)
    currentPlayer=0
    cont()
    
def cont(setPlayer=None):
    global currentPlayer, playerNum, creatureOrder
    if type(setPlayer)==int:
        if setPlayer<playerNum:currentPlayer=setPlayer
        else: return'invalid player number\nautorun ended'
    if type(setPlayer)==str:
        for c in creatureOrder:
            if c.name==setPlayer:
                currentPlayer=creatureOrder.index(c)
    autorun=True
    while autorun:
        if currentPlayer>=playerNum:
            currentPlayer=0
        if creatureOrder[currentPlayer].play()!='next':
            autorun=False
        currentPlayer+=1
    print('autorun ended')


#Test code
Will=player(10,roll(20)+2,'Will')
Mark=player(18,roll(20)+1,'Mark')
Dragon=dragon()
Glenn=player(1,roll(20),'Glenn')
start()
'''Dungeon master commands:
start() starts autoplay
cont() resumes autoplay
cont(player name) resumes autoplay at named players turn --two monsters should not have the same name
cont(player number) resumes autoplay at numbered player/monster turn
target.d(amount) damages the target by a given amount
target.edit(h=health i=initiative) will not automatically change the initiative order
order() orders the creatures based on initiative.'''

