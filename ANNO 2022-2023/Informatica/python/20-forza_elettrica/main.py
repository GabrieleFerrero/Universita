"""
Secondo la legge di Coulomb, la forza elettrica (espressa in Newton) tra due
particelle cariche con carica, rispettivamente, Q1 e Q2, separate da una distanza r, Γ¨
πΉ = (π1 π2)/(4 π π π2)

dove π = 8.854 Γ 10β12 Farad / metro.

Scrivere un programma che calcoli e mostri a video la
forza relativa ad una coppia di particelle cariche, permettendo allβutente di scegliere i valori Q1, Q2
(in Coulomb) e r (in metri).
"""

import math

q1 = float(input("Inserire la carica della particella Q1 (Coulomb): "))
q2 = float(input("Inserire la carica della particella Q2 (Coulomb): "))
r = float(input("Inserire la distanza tra le due particelle (Metri): "))

print(f"La forza elettrica Γ¨: {(q1*q2)/((8.854E-12)*(r**2)*4*math.pi)}")