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


def rotatie(ListaZ, t):
    ListaZ_noua = []
    for z in ListaZ:
        Elait = Trig2Cart(1,t)
        ListaZ_noua.append(z*Elait)
    return ListaZ_noua

plt.clf()
plt.axes().set_aspect('equal')
plt.axhline(y=0, color='r', linestyle='-')  # Axa x
plt.axvline(x=0, color='r', linestyle='-')  # Axa y

# Define the starting points for the green lines
start_point_green1 = -pi/2 + 0j
start_point_green2 = pi/2 + 0j

# Define the lengths of the green lines
length_green = 10

# Generate the green lines
line_green1 = DeseneazaSegment(start_point_green1, start_point_green1 + 1j*length_green, 1000)
line_green2 = DeseneazaSegment(start_point_green2, start_point_green2 + 1j*length_green, 1000)

# Rotate the green lines to align with the horizontal axis
angle_green = 0  # No rotation needed as they are already horizontal

# Plot the green lines
DeseneazaLista(line_green1, culoare="green", marime=10)
DeseneazaLista(line_green2, culoare="green", marime=10)

# Define the starting points for the blue and pink lines
start_point_blue = -1 + 0j
start_point_pink = 1 + 0j

# Define the lengths of the blue and pink lines
length_blue = 10
length_pink = 10

# Generate the blue and pink lines
line_blue = DeseneazaSegment(start_point_blue, start_point_blue + 1j*length_blue, 1000)
line_pink = DeseneazaSegment(start_point_pink, start_point_pink + 1j*length_pink, 1000)

# Rotate the blue line to align with the horizontal axis
angle_blue = -pi/2
multime_blue = line_blue
multime_transformata_blue = rotatie(multime_blue, angle_blue)

# Rotate the pink line to align with the horizontal axis
angle_pink = pi/2
multime_pink = line_pink
multime_transformata_pink = rotatie(multime_pink, angle_pink)

# Plot the blue and pink lines
DeseneazaLista(multime_transformata_blue, culoare="blue")
DeseneazaLista(multime_transformata_pink, culoare="pink")



plt.show()