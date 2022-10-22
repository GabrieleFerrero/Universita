"""
Il decadimento radioattivo dei materiali radioattivi può essere
modellato dall’equazione 𝐴 = 𝐴0𝑒−𝜆𝑡, dove 𝐴 è la quantità di materiale al tempo 𝑡, 𝐴0 è la quantità
al tempo 0 , e 𝜆 è il tasso di decadimento. In particolare 𝜆 = ln 2
𝑇1 2⁄
, dove 𝑇1 2⁄ è l’emivita della
sostanza (espressa nella stessa unità di misura di 𝑡).
Il Tecnezio-99 è un radioisotopo che viene usato per la diagnostica per immagini del cervello. Ha
un’emivita di 6 ore. Scrivere un programma che visualizza la quantità relativa 𝐴/𝐴0 nel corpo di un
paziente per ciascuna ora durante le 24 ore successive alla ricezione della dose
"""

import math

emivita = 67.7

quantita_dose = float(input("Inserire la quantita di dose: "))

for ora in range(24):
    print(f"Quantita rimasta dopo {ora} {'ora' if ora == 1 else 'ore'}: {quantita_dose*((math.e)**(-emivita*ora))}")