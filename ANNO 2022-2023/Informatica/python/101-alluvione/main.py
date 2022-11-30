"""
Si supponga di disporre di una tabella heights di 𝑁 × 𝑁 valori reali che riporta
l’altitudine di un terreno nei diversi punti di un’area quadrata. Scrivere una funzione
flood_map(heights, water_level) che, elaborando una tabella heights di 𝑁 × 𝑁 di
numeri reali che rappresentano le altitudini, e dato il valore water_level del livello dell’acqua,
costruisca e restituisca la mappa di una eventuale inondazione; tale mappa è rappresentata da una
tabella 𝑁 × 𝑁 di stringhe di un carattere ciascuna (asterisco '*' per indicare che la casella è
inondata, o spazio vuoto ' ' per indicare che la casella è all’asciutto).
* * * * * *
* * * * * * * *
* * * * * *
* * * * * * *
* * * * * * * *
* * * * * * * * * *
* * * * * * *
* * * * * *
* *

Poi, scrivere un programma che costruisca una matrice 10x10 di altezze, leggendo 100 valori di
altitudine del terreno, e visualizzi, richiamando la funzione precedente, come il terreno viene
inondato quando il livello dell’acqua cresce. A tal fine, si divida l’intervallo di altezze (dalla minima
alla massima) in 10 intervalli di uguale dimensione, e per ciascuno di questi 10 valori intermedi
(water_level) si stampi la mappa della corrispondente inondazione.
"""

import random

n = 10
altitudini = [[random.randint(0,100) for _ in range(n)] for _ in range(n)]

def print_mappa(mappa):
    for row in mappa:
        for x in row:
            print(f"{x} ", end="")
        print()

def flood_map(heights, water_level):
    mappa = []
    for row in heights:
        riga = []
        for x in row:
            if water_level > x: riga.append("*")
            else: riga.append(" ")
        mappa.append(riga)
    return mappa



for riga in altitudini:
    print(riga)

print()

lista_altitudini = [el for riga in altitudini for el in riga]
min_al = min(lista_altitudini)
max_al = max(lista_altitudini)


for livello_inondazione in range(min_al,max_al, (max_al-min_al)//10):
    print(f"Livello inondazione: {livello_inondazione}")
    mappa = flood_map(altitudini, livello_inondazione)
    print_mappa(mappa)
    print()