"""
Data una lista vuota l = [], scrivere un programma che la riempia con
ciascuna delle sequenze di valori seguenti, dopo aver compreso la regola di generazione della
sequenza (se esiste). [R6.1]
I. 1 2 3 4 5 6 7 8 9 10
II. 0 2 4 6 8 10 12 14 16 18 20
III. 1 4 9 16 25 36 49 64 81 100
IV. 0 0 0 0 0 0 0 0 0 0
V. 1 4 9 16 9 7 4 9 11
VI. 0 1 0 1 0 1 0 1 0 1
VII. 0 1 2 3 4 0 1 2 3 4
"""


lista = []

lista.append([i for i in range(1,11)])
lista.append([i*2 for i in range(0,11)])
lista.append([i**2 for i in range(1,11)])
lista.append([0 for _ in range(0,10)])
lista.append([0 for _ in range(0,10)])
lista.append([i%2 for i in range(0,10)])
lista.append([i%5 for i in range(0,10)])

for riga in lista:
    print(riga)