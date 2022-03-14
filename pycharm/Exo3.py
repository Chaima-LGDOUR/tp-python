prix=float(input('entrez le prix  hors taxes :'))
tva =  18.6
remise=0
if 1000<=prix<2000 :
    print("Prix HT sans réduction : ", prix, "€")
    print("Taux de réduction : 1 %")
    remise=0.09
elif 2000<=prix<5000 :
    print("Prix HT sans réduction : ", prix, "€")
    print("Taux de réduction : 3 %")
    remise=0.07
elif prix>=5000 :
    print("Prix HT sans réduction : ", prix , "€")
    print("Taux de réduction : 5 %")
    remise=0.05

nouveauprix = prix * remise
TIC= nouveauprix*(1+tva/100)
print("Prix HT avec réduction : ", TIC, "€")