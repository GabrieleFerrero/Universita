"""
Scrivere un programma che legga un file di testo (maze.txt) contenente
l’immagine di un labirinto, come il seguente, in cui gli asterischi ('*') rappresentano muri invalicabili
e gli spazi (' ') rappresentano corridoi percorribili.
* *******
* * * *
* ***** *
* * * *
* * *** *
* * *
***** * *
* * *
******* *
Creare un dizionario corridors le cui chiavi sono tuple (riga,
colonna) di posizioni corrispondenti a un corridoio e i cui valori sono
insiemi di posizioni anch’esse corrispondenti a un corridoio, e adiacenti
alla posizione specificata dalla rispettiva chiave. Nell'esempio sopra, la
chiave corrispondente alla tupla (1, 1), evidenziata in blu, ha come
posizioni adiacenti {(1, 2), (0, 1), (2, 1)}. Visualizzare il
dizionario.
"""

percorso = []
with open("maze.txt","r", encoding="utf-8") as file:
    for riga in file:
        percorso.append(list(riga.replace("\n","")))

for riga in percorso:
    print(riga)

corridoi = {}
for y in range(len(percorso)):
    for x in range(len(percorso[y])):

        if percorso[y][x] == " ":
            corridoi[(y,x)] = []

            operazione_su_indice_centrale = [
                [-1, -1], [-1, 0], [-1, +1],
                [0, -1], [0, +1],
                [+1, -1], [+1, 0], [+1, +1]
            ]

            lista_indici = []
            for operazione in operazione_su_indice_centrale:
                if (y + operazione[0] >= 0 and y + operazione[0] <= len(percorso) - 1) and (x + operazione[1] >= 0 and x + operazione[1] <= len(percorso[y]) - 1):
                    lista_indici.append([y + operazione[0], x + operazione[1]])

            for indice in lista_indici:
                if percorso[indice[0]][indice[1]] == " ":
                    corridoi[(y,x)].append((indice[0],indice[1]))

for key,value in corridoi.items():
    print(key, value)

