# **Programmation en Python**

<br>

<p align="center">
  <img width="550" height="400" src="intro.jpg">
</p>

##  Objectif :  Initialisation
<br>


### Exercice 1 :

<p>Ecrire un programme qui permet de décider si un nombre entier saisi est pair ou impair.</p>

<br>
<br>


```java script
print('entrer un nombre')
number = int(input('veuillez entrer un nombre :'))
if number%2==0:
    print('ce nombre et pair')
else:
    print('ce nombre est impair')
```


<br>

### Exercice 2 :

<p>Ecrire un programme qui demande de lire deux nombres entiers et déterminer s'ils sont rangés ou non par 
ordre croissant, et dans tous les cas, afficher leur différence (entre le plus grand et le plus petit)
Le problème peut être résolu en deux étapes.</p>

<br>
<br>


```java script
A=int(input('entrez le premier nombre :'))
B=int(input('entrez le deuxieme nombre'))
MAX=B
if MAX<A :
    print('ils ne sont pas rangés par ordre croissant')
    MAX=A
    D=MAX-B
else :
    print('ils sont rangés par ordre croissant')
    D=MAX-A
print('la difference entre les deux est :',D)
```


<br>


### Exercice 3 :

<p>Ecrire un programme de facturation avec remise. Il lit en donnée un prix hors taxes et calcule le prix TIC 
correspondant (avec un taux de TVA constant de 18,6%). Il établit ensuite une remise dont le taux dépend 
de la valeur ainsi obtenue, à savoir :
• 1% pour un montant supérieur ou égal à 1000 DH et inférieur à 2000DH
• 3% pour un montant supérieur ou égal à 2000 DH et inférieur à 5000DH
• 5% pour un montant supérieur ou égal à 5000 DH
Afficher le prix à payer.</p>

<br>
<br>


```java script
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
```

<br>

### Exercice 4 :

<p>Un magasin de reprographie facture 0,50 Dh les dix premières photocopies, 0,30 Dh les vingt suivantes et 
0,20 Dh au-delà.
Ecrire un programme qui demande à l'utilisateur le nombre de photocopies effectuées et qui affiche la 
facture correspondante.</p>

<br>

<br>


```java script
number=int(input('Nombre de photocopies :'))
facture=number
if number <= 10 :
  facture =number * 0,5
elif number <= 30 :
  facture = 10 * 0,50 + (number-10) * 0,30
else :
  facture = 10 * 0,50 + 20 * 0,30 + (number-30) * 0,20

print('Le prix total est: ', facture )
```


### Exercice 5 :

<p>Ecrire un programme qui permet de résoudre une équation du 2ème degré de la forme : Ax2 + Bx + C = 0, 
En retournant la valeur de x en fonction de A, B et C.</p>

<br>

<br>


```java script
import math
a=int(input('entrez le premier nombre :'))
b=int(input('entrez le deuxieme nombre :'))
c=int(input('entrez le 3 eme nombre :'))
D = b*b - 4*a*c
# Distinction des différents cas
if (a==0 and b==0 and c==0) :# 0x = 0
    print('Tout réel est une solution de cette équation')
elif (a==0 and b==0):  #Contradiction: c # 0 et c = 0
    print('Cette équation ne possède pas de solutions')
elif (a==0): #bx + c = 0
       print('La solution de cette équation du premier degré est :')
       print(' x = ', c/b)
elif (D<0):  # b^2-4ac < 0
     print('Les solutions complexes de cette équation sont les suivantes :')
     print('x1 = ', -b, '+ i*',math.sqrt(-D)/(2*a))
     print('x2 = ', -b, '+ i*',-math.sqrt(-D)/(2*a))
elif (D==0): #b^2-4ac = 0
      print('Cette équation a une seule solution réelle :')
      print(' x =  ', -b/(2*a))
else :# b^2-4ac > 0
       print('Les solutions réelles de cette équation sont :')
       print(' x1 = ', (-b+math.sqrt(D))/(2*a))
       print(' et x2 = ', (-b-math.sqrt(D))/(2*a))
```

### Exercice 6 :

<p>Ecrire un programme qui saisit un nombre puis calcule et affiche sa factorielle.</p>

<br>

<br>


```java script
n=int(input('entrez un nombre :'))
if n == 0:
    print('le factorielle est 1')
else:
    F = 1
    for k in range(2, n + 1):
        F = F * k
    print('le factorielle est ',F)

```

### Exercice 7 :

<p>Ecrire un programme qui saisit successivement 10 nombres et affiche le plus grand parmi eux.
Modifier ensuite le programme pour afficher la position de ce nombre</p>

<br>

<br>


```java script
P = 0
for i in range(1,11) :
  N=int(input('Entrez un nombre :'))
  if (i == 1) or (N > P) :
    P = N
    indice = i

print('Le nombre le plus grand était :',P)
print('Il a été saisi en position numéro ',indice)

```

### Exercice 8 :

<p>Ecrire un programme qui calcule la racine carrée de nombre fournis en données.
Il s'arrêtera lorsqu'on lui fournira la valeur 0. 
Il refusera les valeurs négatives.</p>

<br>

<br>


```java script
from math import sqrt
nbr=input('Donnez un nombre postif : ')
a=float(nbr)
if a>=0 :
   print('La racine carr´ee de ”,a,”vaut ',sqrt(a))
else :
   print('Ceci n’est pas un nombre positif')

```

### Exercice 9 :

<p>Ecrire le programme qui permet de saisir un montant d'argent multiple de 10 DH. 
• Faire un contrôle de saisie bloquant, puis simuler la valeur de ce montant en affichant le nombre de 
billets de 100 DH, 50 DH, et le nombre de pièces de 10 DH autant. 
• Ne pas utiliser la division ni le modulo dans la solution correspondant à cette question.</p>

<br>

<br>


```java script
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
```

### Exercice 10 :

<p>Ecrire un programme qui calcule la puissance nième d'un nombre entier positif saisi. 
La solution doit permettre l'exécution répétitive de ce programme.</p>

<br>

<br>


```java script
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

```

### Exercice 11 :

<p>Ecrire un programme qui demande et contrôle la saisie de 5 nombres premiers. 
A chaque itération, le programme affiche le compteur des nombres premiers restants (5 au début). 
• Si le nombre saisi est premier, alors le programme doit décrémenter le compteur.
• Sinon, il est ignoré et on passe à l'itération suivante.
Le programme s'arrête quand la valeur du compteur devient 0.</p>

<br>

<br>


```java script
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


```
---


<br>


## **Réalisé par : LGDOUR Chaima (CS)**
## **Encadré par : Pr.AMAMOU Ahmed**

<br>

<p align="center">
  <img width="550" height="400" src="merci.jpg">
</p>

---

