"""
Supponiamo che un file contenga le energie e le lunghezze di legame per
dei legami covalenti, come quelli illustrati dalla tabella seguente.
Bond (single |, double ||,
or triple |||)
Bond energy
(kJ/mol)
Bond length
(nm)
C|C 370 0.154
C||C 680 0.13
C|||C 890 0.12
C|H 435 0.11
C|N 305 0.15
C|O 360 0.14
C|F 450 0.14
C|Cl 340 0.18
O|H 500 0.10
O|O 220 0.15
O|Si 375 0.16
N|H 430 0.10
N|O 250 0.12
F|F 160 0.14
H|H 435 0.074
Il formato del file (denominato bond_data.txt) prevede che ogni riga in tabella corrisponda ad
una riga di testo, e che, in ciascuna riga, i tre campi siano separati da uno spazio (' '), e non
prevede l’intestazione. Ad esempio, un file che contiene i dati presentati in tabella potrebbe
contenere il testo:
C|C 370 0.154
C||C 680 0.13
C|||C 890 0.12
...
Scrivere un programma che accetti in input un dato di una colonna e visualizzi i dati dalle altre due
colonne nel file. Se il dato in ingresso ha una corrispondenza con più righe della tabella, il
programma deve restituire i dati delle altre due colonne a tutte le righe che hanno una
corrispondenza col valore in input. Ad esempio, una lunghezza di legame di 0.12 deve restituire sia
il legame triplo C|||C e l’energia di legame 890 kJ/mol, sia il legame singolo N|O e l'energia di
legame 250 kJ/mol.
"""


import csv


with open("bond_data.txt", "r") as csv_file:
    file = csv.reader(csv_file, delimiter=" ")
    contenuto = []
    for riga in file:
        contenuto.append(riga)

dato = input("Inserire dato per ricerca: ")

for riga in contenuto:
    if dato in riga:
        print(riga[0],riga[1],riga[2])
