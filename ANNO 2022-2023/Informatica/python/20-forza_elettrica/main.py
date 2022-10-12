"""
Secondo la legge di Coulomb, la forza elettrica (espressa in Newton) tra due
particelle cariche con carica, rispettivamente, Q1 e Q2, separate da una distanza r, è
𝐹 = (𝑄1 𝑄2)/(4 𝜋 𝜀 𝑟2)

dove 𝜀 = 8.854 × 10−12 Farad / metro.

Scrivere un programma che calcoli e mostri a video la
forza relativa ad una coppia di particelle cariche, permettendo all’utente di scegliere i valori Q1, Q2
(in Coulomb) e r (in metri).
"""

import math

q1 = float(input("Inserire la carica della particella Q1 (Coulomb): "))
q2 = float(input("Inserire la carica della particella Q2 (Coulomb): "))
r = float(input("Inserire la distanza tra le due particelle (Metri): "))

print(f"La forza elettrica è: {(q1*q2)/((8.854E-12)*(r**2)*4*math.pi)}")