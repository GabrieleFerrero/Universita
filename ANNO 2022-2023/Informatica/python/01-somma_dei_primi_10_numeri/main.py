somma = 0

for numero in range(1,10+1): # sommo 1 perché nel ciclo for l'ultimo valore è escluso
    somma += numero

print(somma)

# oppure

import numpy as np

min = int(input("Inserire il numero minimo: "))
max = int(input("Inserire il numero massimo: "))
print(np.arange(min,max+1).sum())
