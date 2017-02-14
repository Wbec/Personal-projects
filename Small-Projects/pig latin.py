VOWELS=["a","e","i","o","u"]
SPACE=" "
words=[]
word=""
x=""

print("This is the pig latin translator")
phrase=input("Insert a word or phrase ")
phrase=phrase.lower()


for letter in phrase:
    if letter==SPACE:
        words.append(word)
        word=""
    else :
        word+=letter
words.append(word)
word=""
phrase=""
for w in words:
    if len(w)>0:
        if w[0] in VOWELS:
            w+="ay "
        else :
            x=w[0]
            w=w[1:]+x+"ay "
        phrase+=w

print(phrase)
input("press enter to exit")
    
        
