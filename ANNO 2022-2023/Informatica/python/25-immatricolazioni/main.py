"""
La matricola degli studenti di un Ateneo è composta da due parti: una
lettera e una sequenza di numeri. Scrivere un programma che, a partire da due codici di matricola, li
mostri a schermo in ordine crescente in base alla sola parte numerica. Suggerimento: utilizzare le
funzioni predefinite del linguaggio Python.
"""


matricola1 = input("Inserire la matricola1: ")
matricola2 = input("Inserire la matricola2: ")


if int(matricola1[1:]) > int(matricola2[1:]):
    print(matricola1)
    print(matricola2)
else:
    print(matricola2)
    print(matricola1)