P = 0
for i in range(1,11) :
  N=int(input('Entrez un nombre :'))
  if (i == 1) or (N > P) :
    P = N
    indice = i

print('Le nombre le plus grand était :',P)
print('Il a été saisi en position numéro ',indice)
