number=int(input('Nombre de photocopies :'))
facture=number
if number <= 10 :
  facture =number * 0,5
elif number <= 30 :
  facture = 10 * 0,50 + (number-10) * 0,30
else :
  facture = 10 * 0,50 + 20 * 0,30 + (number-30) * 0,20

print('Le prix total est: ', facture )
