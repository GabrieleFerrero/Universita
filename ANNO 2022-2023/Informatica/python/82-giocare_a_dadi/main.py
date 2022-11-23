"""
Scrivere un programma che generi una sequenza di 20 lanci casuali di dadi, li
memorizzi in una lista e visualizzi i valori generati, contrassegnando la serie di valori identici più
lunga con questa formattazione:
1 2 5 5 3 1 2 4 3 (2 2 2 2) 3 6 5 5 6 3 1

Se sono presenti più sequenze di valori identici di lunghezza massima, si usi la formattazione indicata
per evidenziare la prima in ordine di occorrenza.
"""

import random

lancio_dadi = []

for _ in range(20): lancio_dadi.append(random.randint(1,6))

print(lancio_dadi)

pezzi = [[lancio_dadi[0], 1, 0]] # numero, lunghezza, indice

# trovo le varie sequenze:
for i in range(1,len(lancio_dadi)):
    if pezzi[-1][0] == lancio_dadi[i]:
        pezzi[-1][1] += 1
    else:
        pezzi.append([lancio_dadi[i], 1, i])


# trovo la più lunga:
indice = 0
max = pezzi[0][1]
for i, el in enumerate(pezzi):
    if el[1] > max:
        max = el[1]
        indice = i

print(f"{str(lancio_dadi[0:pezzi[indice][2]]).replace('[','').replace(']','').replace(',','')}\
 ({str(lancio_dadi[pezzi[indice][2]:(pezzi[indice][2]+pezzi[indice][1])]).replace('[','').replace(']','').replace(',','')}) \
{str(lancio_dadi[(pezzi[indice][2]+pezzi[indice][1]):-1]).replace('[','').replace(']','').replace(',','')}")


