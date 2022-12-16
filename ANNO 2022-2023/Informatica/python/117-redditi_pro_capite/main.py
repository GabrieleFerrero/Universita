"""
Scrivere un programma che legga i dati dal file di testo
rawdata_2004.txt e li inserisca in un dizionario le cui chiavi sono nomi di nazioni e i cui valori
sono redditi annui pro capite. Si noti che nel file i campi sono separati da un carattere di tabulazione
'\t'. Poi, il programma deve chiedere all’utente di fornire in input nomi di nazioni, per visualizzare i
valori corrispondenti di reddito annuo pro capite. Il programma deve terminare quando l’utente
inserisce in input la stringa 'quit'. È possibile leggere dati analoghi, aggiornati al 2021, in formato
.csv, dal file rawdata_2021.csv. Provare a risolvere lo stesso esercizio lavorando su questo file
.csv.
"""

import csv



contenuto = {}
with open("rawdata_2004.txt","r", encoding="utf-8") as file:
    csv_file = csv.reader(file, delimiter="\t")
    for riga in csv_file:
        contenuto[riga[1]] = float(riga[2].replace("$","").replace(",","."))
print(contenuto)

contenuto_aggiornato = {}
with open("rawdata_2021.csv","r", encoding="utf-8") as file:
    csv_file = csv.reader(file, delimiter=",")
    next(csv_file)
    for riga in csv_file:
        contenuto_aggiornato[str(riga[0])] = float(riga[2].replace("$","").replace(",","."))
print(contenuto_aggiornato)


while True:
    print("----------------------------------------")
    nazione = input("Inserire nome nazione: ")
    if nazione == "quit": break
    else:
        if nazione not in contenuto:
            print("Nazione non trovata nei dati vecchi")
        else:
            print(contenuto[nazione])
        if nazione not in contenuto_aggiornato:
            print("Nazione non trovata nei dati aggiornati")
        else:
            print(contenuto_aggiornato[nazione])
