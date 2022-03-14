n=int(input('entrez un nombre :'))
if n == 0:
    print('le factorielle est 1')
else:
    F = 1
    for k in range(2, n + 1):
        F = F * k
    print('le factorielle est ',F)
