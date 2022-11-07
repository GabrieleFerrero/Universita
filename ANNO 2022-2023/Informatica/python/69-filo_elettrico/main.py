"""
Il filo elettrico è un conduttore cilindrico ricoperto da un materiale isolante. La
resistenza di un filo è data dalla formula:
𝑅 = 𝜌𝐿
𝐴 = 4𝜌𝐿
𝜋𝑑2
dove 𝜌 è la resistività del conduttore e 𝐿 , 𝐴 e 𝑑 sono rispettivamente la lunghezza, l’area della
sezione trasversale e il diametro del filo. La resistività del rame è 1,678 × 10−8 Ω𝑚. Il diametro del
filo, 𝑑 , è comunemente specificato dal calibro americano (AWG – american wire gauge), che è un
numero intero, 𝑛 . Il diametro di un filo AWG 𝑛 è dato dalla formula
𝑑 = 0.127 × 92 36 − 𝑛
39 𝑚𝑚
Scrivere una funzione
def diameter(wire_gauge)
che accetti il calibro del filo e restituisca il diametro corrispondente. Scrivere un'altra funzione
def copper_wire_resistance(length, wire_gauge)
che accetti la lunghezza e il calibro di un pezzo di filo di rame e ne restituisca la resistenza.
La resistività dell'alluminio è 2,82 × 10−8 Ω𝑚. Scrivere una terza funzione
def aluminum_wire_resistance(length, wire_gauge)
che accetti la lunghezza e il calibro di un pezzo di filo di alluminio e ne restituisca la resistenza.
Scrivere poi un programma per testare queste funzioni.
"""

import math

resistivita_rame = 1.678E-8
resistivita_alluminio = 2.82E-8

def diameter(wire_gauge):
    return 0.127*(92**((36-wire_gauge)/39))

def copper_wire_resistance(length, wire_gauge):
    return (4*resistivita_rame*length)/(math.pi*(diameter(wire_gauge)**2))

def aluminum_wire_resistance(length, wire_gauge):
    return (4 * resistivita_alluminio * length) / (math.pi * (diameter(wire_gauge) ** 2))


lunghezza = float(input(("Inserire lunghezza filo: ")))
calibro = int(input("Inserire calibro: "))

print(diameter(calibro))
print(copper_wire_resistance(lunghezza, calibro))
print(aluminum_wire_resistance(lunghezza, calibro))

