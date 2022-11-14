"""
Scrivere un programma che inizializzi una lista con dieci numeri interi
casuali tra 1 e 100 e poi visualizzi, su quattro righe successive:
I. Tutti gli elementi di indice pari;
II. Tutti gli elementi di valore pari;
III. Tutti gli elementi in ordine inverso;
IV. Il primo e l’ultimo elemento.
"""

import random

numeri = []
for _ in range(10): numeri.append(random.randint(1,100))

print(numeri)

print("Numeri con indice pari: ")
for i,num in enumerate(numeri):
    if i%2 == 0: print(f"{num} ", end="")


print("\nNumeri pari: ")
for num in numeri:
    if num%2 == 0: print(f"{num} ", end="")

print(f"\nNumeri in ordine inverso: {numeri[::-1]}")

print(numeri[0])
print(numeri[-1])