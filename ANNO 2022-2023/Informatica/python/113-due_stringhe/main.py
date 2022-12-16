"""
Scrivere un programma che chieda all’utente di fornire due stringhe, per poi
visualizzare (evitando ripetizioni di caratteri nella stampa):
I. i caratteri che compaiono in entrambe le stringhe;
II. i caratteri che compaiono in una stringa ma non nell’altra;
III. le lettere (alfabetiche) che non compaiono in nessuna delle due stringhe.
Suggerimento: utilizzare la funzione set() per trasformare una stringa in un insieme di caratteri.
"""

import string

stringa_1 = input("Inserire stringa 1: ")
stringa_2 = input("Inserire stringa 2: ")

insieme_1 = set(stringa_1)
insieme_2 = set(stringa_2)
insieme_3 = set(string.ascii_letters)

print(insieme_1.intersection(insieme_2))
print(insieme_1.difference(insieme_2))

insieme_1 = set(stringa_1.replace(" ",""))
insieme_2 = set(stringa_2.replace(" ",""))
print(insieme_3.difference(insieme_1.union(insieme_2)))