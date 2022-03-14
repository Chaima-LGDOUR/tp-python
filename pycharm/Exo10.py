def fonction(n,p):
 if n==0 :
   exp = 1
 else:
   exp= fonction(n-1,p)*p
 return(exp)

p = int(input('veuillez entrer un nombre :'))
n = int(input('veuillez entrer la puissance :'))
m=fonction(n,p)
print(m)
