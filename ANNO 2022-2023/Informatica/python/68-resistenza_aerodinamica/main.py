"""
La forza di resistenza aerodinamica su un'automobile è data da:
𝐹𝐷 = 1
2 𝜌𝜐2𝐴𝐶𝐷

dove 𝜌 è la densità dell’aria (1,23 𝑘𝑔/𝑚3), 𝜐 è la velocità in 𝑚/𝑠 , 𝐴 è l’area proiettata dell’auto
(2,5 𝑚2) e 𝐶𝐷 è il coefficiente di resistenza aerodinamica (0,2 ). La quantità di potenza in watt
necessaria per vincere la forza di resistenza è 𝑃 = 𝐹𝐷𝜐 , e la potenza equivalente in cavalli è 𝐻𝑝 =
𝑃/745.7 . Scrivere un programma che accetti la velocità dell’auto e calcoli la potenza in watt e in
cavalli necessaria per superare la forza di resistenza risultante.
"""

import math

p = 1.23
A = 2.5
Cd = 0.2

def calcolo_potenza(v):
    Fd = (1/2)*p*(v**2)*A*Cd

    watt = Fd*v
    horse = watt/745.7

    return watt, horse



velocita = float(input("Inserire la velocità: "))
print(calcolo_potenza(velocita))
