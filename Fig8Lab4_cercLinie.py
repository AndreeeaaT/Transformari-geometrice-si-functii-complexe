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

# Desenam un cerc

def DeseneazaCerc(z0, r, NumarPuncte = 100):
    ListaZ = []
    for k in range(NumarPuncte):
        theta = 2*pi*k/NumarPuncte
        z = z0 + Trig2Cart(r,theta)
        ListaZ.append(z)
    return ListaZ
def inversiune(ListaZ):
    Lista_noua = []
    for z in ListaZ:
        if z != 0:
            Lista_noua.append(1/z)
    return Lista_noua


cerc = DeseneazaCerc(1.5-1.5j,3)
multime = cerc
multime_transformata = inversiune(multime)

plt.clf()
plt.axes().set_aspect('equal')
plt.axhline(y=0, color='r', linestyle='-')
plt.axvline(x=0, color='r', linestyle='-')

DeseneazaLista(multime,culoare="blue", marime=5)
DeseneazaLista(multime_transformata,culoare="red")
plt.show()
