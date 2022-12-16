"""
Il responsabile amministrativo di un albergo registra le vendite in un file di testo.
Ogni riga contiene le seguenti 4 informazioni, separate da caratteri punto e virgola (';'):
I. il nome del cliente;
II. il servizio venduto;
III. l’importo pagato;
IV. la data dell’evento.
I servizi venduti possono essere, ad esempio, una cena, una conferenza, oppure un alloggio. Il
formato corretto per questo file prevede che contenga 4 campi per riga, e che l’importo pagato
contenga valori di tipo float. Scrivere un programma che legga questo file di testo, e visualizzi
l’importo totale relativo a ciascun tipo di servizio, segnalando un errore se il file non esiste oppure se
il suo formato non è corretto.
"""

import csv


def is_float(number):
    try:
        _ = float(number)
        return True
    except:
        return False

try: csv_file = open("input.txt", "r", encoding="utf-8")
except: exit("File non trovato")

file = csv.reader(csv_file, delimiter=';')
importi = {}
for i, riga in enumerate(file):
    servizio = riga[1].replace(" ", "")
    prezzo = riga[2]

    if len(riga) != 4: print(f"Numero di colonne non giuste per la riga n°{i+1}")
    else:
        if not is_float(prezzo): print(f"Prezzo non corretto alla riga n°{i+1}")
        else:
            if servizio in importi: importi[servizio] += float(prezzo)
            else: importi[servizio] = float(prezzo)



for servizio, somma in importi.items():
    print(servizio, somma)

csv_file.close()