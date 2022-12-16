"""
Il filo di Arianna deve la sua fama al mito di Minosse e del Labirinto. Esso,
infatti, servì a Teseo per trovare l'uscita dal labirinto di Minosse, tracciando ad ogni bivio la direzione
verso l’uscita. Estendere il programma dell’esercizio 11.2.3 in modo che, a partire da un punto
qualsiasi, trovi una via d’uscita dal labirinto, ad esempio utilizzando il seguente algoritmo:.
Basandosi sul dizionario corridors, costruire un nuovo dizionario paths le cui chiavi
sono tuple (riga, colonna) di posizioni corrispondenti a un corridoio e i cui valori sono
inizialmente tutti uguali alla stringa '?'. Poi, scorrere le chiavi del dizionario paths e, per
ogni chiave che rappresenti posizioni ai bordi del labirinto, e che quindi corrisponda ad
un’uscita, sostituire la stringa '?' con una stringa che indichi la direzione del percorso di
uscita: 'N' (per 'North'), 'E' (per 'East'), 'S' (per 'South') o 'W' (per 'West').
Fatta questa sostituzione, utilizzando il dizionario corridors per localizzare le posizioni
adiacenti, scorrere le chiavi del dizionario paths il cui valore è ancora '?'. Per ciascuna di
queste posizioni, verificare se hanno almeno una posizione adiacente il cui valore in paths è
diverso da '?'. In caso affermativo, sostituire la stringa '?' con una stringa che indica la
direzione verso la quale si trova la posizione adiacente individuata.
Esempio: la chiave corrispondente alla tupla (1, 1) ha come posizioni adiacenti {(1,
2), (0, 1), (2, 1)}. Se alla chiave (0, 1) è stato assegnato il valore 'N', nel
dizionario paths, se all’iterazione corrente il valore assegnato alla chiave (1, 1) è ancora
'?', poiché nella posizione adiacente c’è un valore diverso da'?', verrà assegnato il valore
'N', in quanto la posizione adiacente in questione si trova in direzione 'North'.
Se durante una delle iterazioni di scorrimento di chiavi e valori non è possibile compiere
sostituzioni, concludere l’esecuzione del programma.
Infine, visualizzare il labirinto ottenuto, dove in ciascuna posizione di corridoio è indicata la direzione
che porta più rapidamente a un’uscita. Ad esempio:
*N*******
*NWW*?*S*
*N*****S*
*N*S*EES*
*N*S***S*
*NWW*EES*
*****N*S*
*EEEEN*S*
*******S*
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
                         [-1, 0],
                [0, -1],            [0, +1],
                         [+1, 0]
            ]

            lista_indici = []
            for operazione in operazione_su_indice_centrale:
                if (y + operazione[0] >= 0 and y + operazione[0] <= len(percorso) - 1) and (x + operazione[1] >= 0 and x + operazione[1] <= len(percorso[y]) - 1):
                    lista_indici.append([y + operazione[0], x + operazione[1]])

            for indice in lista_indici:
                if percorso[indice[0]][indice[1]] == " ":
                    corridoi[(y,x)].append((indice[0],indice[1]))

"""print()
for key,value in corridoi.items():
    print(key, value)"""

paths = {key:"?" for key in corridoi}
"""print()
for key,value in paths.items():
    print(key, value)"""

for key,value in paths.items():
    y = key[0]
    x = key[1]

    if x == 0:
        paths[(y,x)] = "W"
    elif x == len(percorso[y])-1:
        paths[(y, x)] = "E"
    elif y == 0:
        paths[(y, x)] = "N"
    elif y == len(percorso)-1:
        paths[(y, x)] = "S"

"""print()
for key,value in paths.items():
    print(key, value)"""

while True:
    sostituzione = False
    for key, value in paths.items():
        if value=="?":
            if len(corridoi[key]) > 0:
                # ci sono spazi disponibili
                for cella in corridoi[key]:
                    if paths[cella] != "?":
                        if cella[1] > key[1]:
                            paths[key] = "E"
                        elif cella[1] < key[1]:
                            paths[key] = "W"
                        elif cella[0] > key[0]:
                            paths[key] = "S"
                        elif cella[0] < key[0]:
                            paths[key] = "N"
                        sostituzione = True
    if not sostituzione: break



for y in range(len(percorso)):
    for x in range(len(percorso[y])):
        if (y,x) in paths:
            percorso[y][x] = paths[(y,x)]


print()
for riga in percorso:
    print(riga)