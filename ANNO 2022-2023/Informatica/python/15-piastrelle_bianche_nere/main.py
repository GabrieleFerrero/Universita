"""
Bisogna posizionare lungo il muro una fila di piastrelle nere e bianche. Per
ragioni estetiche l'architetto ha specificato che la prima e l’ultima piastrella
devono essere nere. Il vostro compito è calcolare il numero di piastrelle
necessarie e il vuoto a ciascuna delle due estremità della riga, dato lo spazio
disponibile e la larghezza di ogni piastrella.
"""

import math

lun = 100 # lunghezza muro da piastrellare
lato = 1 # lunghezza lato piastrella

num_piastrelle = int(lun/lato)

# RISOLVERE SISTEMA DI EQUAZIONI:
# x --> numero di piastrelle nere , y --> numero di piastrelle bianche

# x = y + 1
# y + x = num_piastrelle

# x = num_piastrelle - x + 1
# 2x = num_piastrelle + 1
# x = (num_piastrelle +1)/2

x = (num_piastrelle + 1)/2
y = num_piastrelle - x

x = int(x)
y = int(y)

print(f"numero piastrele nere: {x}")
print(f"numero piastrele bianche: {y}")
print(f"spazio da ogni lato: {(lun-(x+y))/2}")