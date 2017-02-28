import pickle

file=open('prime num pickle',"rb")

def loadall(file):
    '''Loads only from files with the format created by pickle_saver.save'''
pickle.load(

for item in range(length):
    primes.append(pickle.load(file))
file.close()
autosave=0


except KeyboardInterrupt:
    file=open('prime num pickle',"wb")
    pickle.dump(len(primes),file)
    for j in primes:
        pickle.dump(j,file)
    file.close()
    raise RuntimeError("Quiting complete")
