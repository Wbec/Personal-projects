from quiter import QuitError

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
            if response=='q':
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
                    print('reply with:', answerType)#improve (with dictionary?)              
            else:
                return None

def choose (options, prompt='', end='',indexStart=0, runs=1, extra=True):
    'set runs to -1 for infinite.'
    while runs !=0:
        print (prompt)
        index=indexStart
        for option in options:
            print (index,option,sep='--')
            index+=1
        try:
            response=input(end)
            if response== 'q':
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
                return None

    
