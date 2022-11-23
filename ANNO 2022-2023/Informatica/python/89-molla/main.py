"""
Scrivere un programma che modelli e simuli il movimento di un oggetto di
massa 𝑚 collegato ad una molla oscillante. Quando la molla viene spostata dalla sua posizione di
equilibrio di una quantità 𝑥 , la legge di Hooke afferma che la forza di ripristino è data dalla formula:
𝐹 = −𝑘𝑥
dove 𝑘 è una costante che dipende dalla molla. Per questa simulazione, utilizzare k = 10 N/m.
Iniziare con un determinato spostamento 𝑥 (ad esempio, x = 0.5 m). Impostare la velocità
iniziale v = 0. Calcolare l’accelerazione 𝑎 in base alla legge di Newton (𝐹 = 𝑚𝑎 ) e alla legge di
Hooke, utilizzando una massa m = 1 kg. Utilizzare un piccolo intervallo di tempo delta_t =
0.01 s e, ad ogni passo, aggiornare la velocità, calcolando una variazione di 𝑎Δ𝑡 , e lo spostamento,
calcolando una variazione di 𝑣Δ𝑡 .
"""

import math
from matplotlib import pyplot as plt

# F = -k*x
# m*a = -k*x
# a = (-k*x)/m
# a = m / s^2

k = 10 # N/m
x = 0.5 # metri
m = 1 # kilogrammi
delta_t = 0.01 # secondi
costante_moltiplicativa = 10**(int(abs(math.log10(delta_t)))+1)

x_dati = []
valori_velocita = []
valori_spazio = []
for tempo in range(0,10000 , int(delta_t*costante_moltiplicativa)):

    tempo /= costante_moltiplicativa

    x_dati.append(tempo)

    a = (-k * x) / m

    valori_velocita.append(a*tempo)
    x = valori_velocita[-1]*tempo
    valori_spazio.append(x)



plt.plot(x_dati, valori_velocita, "-b", label="velocità")
plt.plot(x_dati, valori_spazio, "-r", label="spazio")
plt.legend(loc="upper left")
plt.show()