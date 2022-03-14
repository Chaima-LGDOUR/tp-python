def isitPrime(k):
    if k==2 or k==3: return True
    if k%2==0 or k<2: return False
    for i in range(3, int(k**0.5)+1, 2):
        if k%i==0:
            return False

    return True

pos=0
counter=5
while counter!=0 :
    n = int(input('entrer un nombre premier : '))
    premiere = isitPrime(n)
    if premiere== True:
        counter=counter-1
    else:
        pos=pos+1


    print('il vous reste encore', counter)

