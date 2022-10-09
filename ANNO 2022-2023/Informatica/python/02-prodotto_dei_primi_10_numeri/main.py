prodotto = 1

for numero in range(1,10+1): # sommo 1 perché nel ciclo for l'ultimo valore è escluso
    prodotto *= numero

print(prodotto)

# oppure

import numpy as np

min = int(input("Inserire il numero minimo: "))
max = int(input("Inserire il numero massimo: "))
print(np.arange(min,max+1).prod())
