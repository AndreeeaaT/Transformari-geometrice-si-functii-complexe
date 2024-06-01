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
def rotatie_complex(ListaZ, t):
    ListaZ_noua = []
    for z in ListaZ:
        Elait = Trig2Cart(1, t.real)  # Use the real part of the complex angle
        ListaZ_noua.append(z * Elait)
    return ListaZ_noua
patrat = DeseneazaSegment(0+0j, 0.5+0j) + DeseneazaSegment(0.5+0j, 0.5+0.5j) + DeseneazaSegment(0.5+0.5j, 0+0.5j) + DeseneazaSegment(0+0.5j, 0+0j)
multime = patrat
multime_transformata = rotatie_complex(multime, 0.2+1.5j)

plt.clf()
plt.axes().set_aspect('equal')
plt.axhline(y=0, color='r', linestyle='-')
plt.axvline(x=0, color='r', linestyle='-')

DeseneazaLista(multime,culoare="blue", marime=5)
DeseneazaLista(multime_transformata,culoare="red")

plt.show()