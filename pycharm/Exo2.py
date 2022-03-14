A=int(input('entrez le premier nombre :'))
B=int(input('entrez le deuxieme nombre'))
MAX=B
if MAX<A :
    print('ils ne sont pas rangés par ordre croissant')
    MAX=A
    D=MAX-B
else :
    print('ls sont rangés par ordre croissant')
    D=MAX-A
print('la difference entre les deux est :',D)