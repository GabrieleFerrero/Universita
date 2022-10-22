"""
Scrivere un programma che chieda all’utente un numero intero e, poi, visualizzi
tutti i numeri primi minori o uguali a tale numero. Se, ad esempio, l’utente fornisce il numero 20, il
programma deve visualizzare:
2
3
5
7
11
13
17
19
"""

import math

numero = int(input("Inserire numero: "))

numero = abs(numero)

primi = []

for c in range(2, numero):
    primo = True
    for n in range(2, int(math.sqrt(c))+1):
        if c%n==0:
            primo=False
            break

    if primo: primi.append((c))

print(primi)
