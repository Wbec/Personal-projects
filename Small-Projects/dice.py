dice=(1,2,3,4,5,6)
totals=[]
for a in dice:
    for b in dice:
        for c in dice:
            for d in dice:
                low=a
                for die in (b,c,d):
                    if die<low:
                        low=die
                total=a+b+c+d-low
                totals.append(total)
average=0
for n in range(3,19):
    count=0
    for m in totals:
        if n==m:
            count+=1
    print(str(n),str(count))
    average+=n*count/1296
print(average)
print((8+10+12+15+14+13)/6)
