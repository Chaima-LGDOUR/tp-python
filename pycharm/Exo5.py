
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