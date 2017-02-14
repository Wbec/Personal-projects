import time
import pickle

file=open('prime num pickle',"rb")

primes=[]
try:
    length=pickle.load(file)
except EOFError:
    length=0

for item in range(length):
    primes.append(pickle.load(file))
file.close()
autosave=0

if primes:
    current=primes[-1]
else:
    current=1
try:
    while True:
        time.sleep(0.002)
        bad=0
        current+=1
        autosave+=1
        for i in primes:
            if current%i==0:
                bad=1
                break
        if bad==0:
            primes.append(current)
            print(current)
        if autosave==250:
            file=open('prime num pickle',"wb")
            pickle.dump(len(primes),file)
            for j in primes:
                pickle.dump(j,file)
            file.close()
            autosave=0

    
except KeyboardInterrupt:
    file=open('prime num pickle',"wb")
    pickle.dump(len(primes),file)
    for j in primes:
        pickle.dump(j,file)
    file.close()
    raise RuntimeError("Quiting complete")
