done=False
while done==False:
    goodnum=False
    while goodnum==False:
        try:
            inp=input("input a number or type quit:")
            if inp=='quit':
                done=True
                num=0
                break
            num=int(inp)
        except ValueError:
            goodnum=False
        else:
            goodnum=True


    result=""
    for x in range(3,0,-1):
        multi=10**(x)
        if multi==1000:
            hi,fiv,lo='M','D','C'
        if multi==100:
            hi,fiv,lo='C','L','X'
        if multi==10:
            hi,fiv,lo='X','V','I'
        if num>=multi:
            result+=hi*int(num/multi)
            num-=multi*int(num/multi)
        if num>=0.9*multi:
            result+=lo+hi
            num-=0.9*multi
        if num>=0.5*multi:
            result+=fiv
            num-= 0.5*multi
        if int(num/(multi/10))==4:
            result+=lo+fiv
            num-=0.4*multi
        if num>=multi/10:
            result+=lo*int(num/(multi/10))
            num-=(multi/10)*int(num/(multi/10))
    print(result)
