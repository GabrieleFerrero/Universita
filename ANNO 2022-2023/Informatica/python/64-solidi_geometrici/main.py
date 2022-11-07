"""
Scrivere le funzioni:
def sphere_volume(r)
def sphere_surface(r)
def cylinder_volume(r, h)
def cylinder_surface(r, h)
def cone_volume(r, h)
def cone_surface(r, h)

che calcolino il volume e la superficie di una sfera di raggio 𝑟 , di un cilindro a base circolare di raggio
𝑟 e altezza ℎ , e di un cono a base circolare con raggio 𝑟 e altezza ℎ . Poi scrivere un programma che
chieda all’utente i valori di 𝑟 e ℎ , chiami le sei funzioni e visualizzi i risultati in output.
"""

import math

def sphere_volume(r):
    return (4/3)*math.pi*(r**3)

def sphere_surface(r):
    return 4*math.pi*(r**2)

def cylinder_volume(r, h):
    return (math.pi*(r**2))*h

def cylinder_surface(r, h):
    return ((math.pi*(r**2))*2) + (2*math.pi*2*h)

def cone_volume(r, h):
    return (math.pi*(r**2)*h)/3

def cone_surface(r, h):
    return math.pi*r*(r+(math.sqrt((h**2)+(r**2))))


h = float(input("Inserire il valore di h: "))
r = float(input("Inserire il valore di r: "))

print(sphere_volume(r))
print(sphere_surface(r))
print(cylinder_volume(r,h))
print(cylinder_surface(r,h))
print(cone_volume(r,h))
print(cone_surface(r,h))
