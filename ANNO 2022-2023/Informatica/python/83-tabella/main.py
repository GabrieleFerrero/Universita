"""
Scrivere le istruzioni Python per eseguire le seguenti operazioni con una tabella
di 𝑚 righe e 𝑛 colonne (dimensioni inserite da tastiera):
I. inizializzare la tabella con valori pari a zero (0);
II. riempire tutte le caselle con valori pari a uno (1);
III. riempire le caselle alternando 0 e 1 in uno schema a scacchiera;
IV. riempire di 0 solo le caselle della riga superiore e di quella inferiore, lasciando invariato il
resto della tabella;
V. riempire con 1 solo le caselle della colonna di destra e di sinistra, lasciando invariato il resto
della tabella;
VI. calcolare e stampare la somma di tutti gli elementi.
Dopo ogni operazione, stampare la tabella.
"""


def print_tabella(tabella):
    print("[")
    for riga in tabella:
        print(riga)
    print("]\n")

num_righe = int(input("Inserire num righe: "))
num_colonne = int(input("Inserire num colonne: "))

# I
tabella = [[0]*num_colonne for _ in range(num_righe)]

print_tabella(tabella)

# II
for num_riga in range(num_righe):
    for num_colonna in range(num_colonne):
        tabella[num_riga][num_colonna] = 1

print_tabella(tabella)

# III
for num_riga in range(num_righe):
    for num_colonna in range(num_colonne):
        if (num_riga+num_colonna)%2 ==0: tabella[num_riga][num_colonna] = 0
        else: tabella[num_riga][num_colonna] = 1

print_tabella(tabella)

# IV
for i in range(num_colonne):
    tabella[0][i] = 0
    tabella[-1][i] = 0

print_tabella(tabella)

# V
for num_riga in range(num_righe):
    for num_colonna in range(num_colonne):
        if num_colonna == 0 or num_colonna == num_colonne-1: tabella[num_riga][num_colonna] = 1

print_tabella(tabella)

# VI
somma = 0
for num_riga in range(num_righe):
    for num_colonna in range(num_colonne):
        somma += tabella[num_riga][num_colonna]

print(somma)