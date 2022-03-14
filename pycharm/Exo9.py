argent=int(input('saisir la somme d argent: ' ))
i=0
n=argent
while(n>=100):
   n=n-100
   i=i+1

argent=argent-i*100
j=0
k = 0
n=argent
if n!=0:
  while(n>=50):
   n=n-50
   j=j+1
   argent=argent-j*50
   k=0
   n=argent
   if n!=0:
       while(n>=10):
           n=n-10
           k=k+1
print('Il faut ', j,'billets de 50 DH')
print('Il faut ', i,'billets de 100 DH')
print('Il faut ', k,'billets de 10 DH')