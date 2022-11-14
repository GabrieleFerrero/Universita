"""
Scrivere un programma che generi una sequenza di 20 valori interi casuali
compresi tra 0 e 99, poi visualizzi la sequenza generata, la ordini e la visualizzi di nuovo, ordinata.
Usate il metodo sort().
"""

import random

lista = []
for _ in range(20):
    lista.append(random.randint(0,99))

print(lista)
print(sorted(lista))