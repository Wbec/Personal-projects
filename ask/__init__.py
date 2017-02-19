from quitter import QuitError
#add yes or no-->True or False

class AskError (Exception):
    'base error for ask module'
    pass

class TypeNotIncludedError (AskError):
    def __init__(self,answerType):
        self.answerType=answerType
        
    def __str__(self): 
        return('answer type '+self.answerType+' is not valid for ask module.')

def ask(answerType, prompt='', runs=1, extra=True):
    'set runs to -1 for infinite.'
    while runs !=0: 
        response=input(prompt)
        try:
            if response=='quit':
                raise QuitError
            if answerType== 'str':
                return response
            elif answerType== 'int':
                return int(response)
            elif answerType== 'float':
                return float(response)
            elif answerType== 'bool':
                return bool(response)
            else:
                raise TypeNotIncludedError(answerType)
        except ValueError:
            if runs!=0:
                if runs>0:runs-=1
                if extra:
                    print('reply with:', answerType)              
            else:
                return None

def choose (optionsList, prompt='', end='',indexStart=0, runs=1, extra=True): #Untested
    'Set runs to -1 for infinite.' 
    d={}
    index=indexStart
    for option in optionsList:
        d[str(index)]=option
        index+=1
    return options(d,prompt,end,runs,extra)
                   
                
"""def choose (options, prompt='', end='',indexStart=0, runs=1, extra=True): #tested, old
    #merge choose into options at some point?
    while runs !=0:
        print (prompt)
        index=indexStart
        for option in options:
            print (index,option,sep='--')
            index+=1
        try:
            response=input(end)
            if response== 'quit':
                raise QuitError
            response=int(response)
            if response <0: raise IndexError
            choice=options[response-indexStart]
            return choice
        except (ValueError,IndexError):
            if runs!=0:
                if extra and runs!=1:
                    print('reply with a whole number between', indexStart, 'and', index-1,)
                if runs!=-1:runs-=1
            else:
                return None"""


def options (d, prompt='', end='', runs=1, extra=True):
    'Dictionary based input. Set runs to -1 for infinite. Keys should be strings'
    while runs !=0:
        print (prompt)
        for key in d.keys():
            print (key,'--',d[key])
        try:
            response=input(end)
            if response== 'quit':
                raise QuitError
            else:
                return d[response]
        except KeyError:
            if runs!=0:
                if extra and runs!=1:
                    print('reply with one of the options (before the dash)')
                if runs!=-1:runs-=1
            else:
                return None
            
    
