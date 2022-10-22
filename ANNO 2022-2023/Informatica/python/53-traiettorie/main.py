"""
Supponiamo che una palla di cannone sia proiettata in aria con una velocità
iniziale 𝜐0. Qualunque libro di fisica affermerà che la posizione della palla dopo 𝑡 secondi è 𝑠(𝑡) =
− 1
2 𝑔𝑡2 + 𝜐0𝑡, dove 𝑔 = 9.81 𝑚/𝑠2 è l’accelerazione di gravità della Terra. Nessun libro di
matematica menziona però perché qualcuno dovrebbe avere intenzione di procedere con questo
esperimento chiaramente pericoloso; quindi, noi lo svolgeremo in totale sicurezza, con l’aiuto del
computer. Infatti, confermeremo la teoria con l’aiuto di una simulazione. Nella nostra simulazione,
considereremo come la palla si sposta in intervalli di tempo molto piccoli Δ𝑡 . In un piccolo intervallo
di tempo, la velocità 𝜐 è praticamente costante, e possiamo calcolare la distanza percorsa dalla palla
come Δ𝑠 = 𝜐Δ𝑡 . Scrivere un programma che imposti la costante DELTA_T = 0.01 (secondi) e
aggiorni la posizione della palla con:
s = s + v * DELTA_T.
La velocità cambia costantemente, in quanto viene ridotta dalla forza gravitazionale della Terra. In
un piccolo intervallo di tempo, Δ𝜐 = − 𝑔Δ𝑡 , dunque, dobbiamo tenere la velocità aggiornata con:
v = v – g * DELTA_T.
In ciascuna iterazione successiva, il nuovo valore di velocità è utilizzato per aggiornare il calcolo della
distanza percorsa. Il programma deve continuare l’esecuzione della simulazione fino a quando la
palla di cannone cade a terra. Il programma prende in input la velocità iniziale (ad esempio, 100
metri al secondo). Aggiorna la posizione e la velocità 100 volte per ogni secondo simulato, ma
visualizza in output la posizione calcolata solamente una volta per secondo simulato, insieme al
valore calcolato dalla formula esatta 𝑠(𝑡) = − 1
2 𝑔𝑡2 + 𝜐0𝑡, per confronto.
Nota: potrebbe sorgere un dubbio sul motivo per cui è vantaggioso simulare un fenomeno per cui
esiste una formula esatta. Il motivo è che la formula non è veramente esatta. Ad esempio,
l’accelerazione di gravità varia a seconda della distanza dalla Terra. Questo non è rappresentato
dalla formula, mentre la nostra simulazione potrebbe essere estesa per includere questo aspetto.
Per questo la simulazione si rende necessaria per le traiettorie di oggetti che volano più in alto, ad
esempio i missili.
"""

from matplotlib import pyplot as plt

DELTA_T = 0.01
g = 9.81
spazio_simulazione=0
spazio_formula=0
tempo_trascorso = 1
velocita_simulazione=[]

v_0 = float(input("Inserire la velocità: "))
v=v_0


while True:
    for _ in range(100):
        v = v - g * DELTA_T
        velocita_simulazione.append(abs(v))
        spazio_simulazione = spazio_simulazione + v * DELTA_T

    if spazio_simulazione < 0: break

    print(f"Spazio percorso secondo la simulazione: {spazio_simulazione}")
    print(f"Spazio percorso secondo la formula: {-(1/2)*g*(tempo_trascorso**2) + v_0*tempo_trascorso}")
    print("-------------------------------------------------------")

    tempo_trascorso += 1


plt.plot(velocita_simulazione)
plt.show()
