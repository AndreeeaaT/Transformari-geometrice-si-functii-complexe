from math import *

# 5 Conversie coordonate polare/trigonometrice în coordonate carteziene
def Trig2Cart(modul,argument):
    x = modul*cos(argument)
    y = modul*sin(argument)
    z = x + 1j*y
    return z

def Cart2Trig(z):
    x = z.real
    y = z.imag
    print(x)
    print(y)
    modul = sqrt(x*2 + y*2)
    argument = atan2(y,x)
    return (modul,argument)

# Desenam o lista de puncte in plan (de afixe)

import matplotlib.pyplot as plt

def DeseneazaLista(ListaZ, culoare = 'blue', marime = 10):
    for z in ListaZ:
        x = z.real
        y = z.imag
        plt.scatter(x,y, color = culoare, s = marime)
    return
# Desenam un segment cu capete date

def DeseneazaSegment(z1, z2, NumarPuncte = 100):
    ListaZ = []
    for k in range(NumarPuncte):
        t = k/NumarPuncte
        z = (1-t)*z1+t*z2
        ListaZ.append(z)
    return ListaZ
def translatie(ListaZ,b):
    ListaZ_noua = []
    for z in ListaZ:
        ListaZ_noua.append(z+b)
    return ListaZ_noua

linie1=DeseneazaSegment(-5,5,100)
linie2=DeseneazaSegment(-5+pi*1j, 5+pi*1j,100)

multime=linie2
multime_transformata=translatie(multime, 0-pi*1j)

plt.clf()
plt.axes().set_aspect('equal')
plt.axhline(y=0, color='r', linestyle='-')
plt.axvline(x=0, color='r', linestyle='-')
DeseneazaLista(linie1, 'blue',10)
DeseneazaLista(linie2,'blue',10)
DeseneazaLista(multime_transformata,'red',10)

plt.show()