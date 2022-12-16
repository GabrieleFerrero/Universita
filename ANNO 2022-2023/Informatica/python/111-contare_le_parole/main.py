"""
Scrivere un programma che conti le occorrenze di ciascuna parola presente
in un file di testo, il cui nome è inserito in input. Si assuma che il file contenga solo caratteri alfabetici
o di spaziatura (come ad esempio il file input.txt). Il programma deve visualizzare tutte le parole
presenti, con a fianco il numero di occorrenze di ciascuna.
"""

nome_file = input("Inserire nome file: ")


conteggio_parole = {}
with open(nome_file, "r") as file:
    for line in file:
        for parola in line.split():
            if parola in conteggio_parole: conteggio_parole[parola] += 1
            else: conteggio_parole[parola] = 1


for parola, numero in conteggio_parole.items():
    print(parola, numero)
