"""
Scrivere un programma che gestisca la prevendita di un numero limitato di biglietti
del cinema. Ogni acquirente può comprare al massimo 4 biglietti e non ne possono essere venduti
più di 100 in totale. Il programma deve chiedere all’utente quanti biglietti intende acquistare, per
poi visualizzare il numero di biglietti rimasti. L’operazione va ripetuta fino all’esaurimento dei
biglietti, visualizzando al termine il numero di acquirenti.
"""

max_biglietti = 180
max_biglietti_acquistabili_singolo_utente = 4

num_acquirenti = 0

while max_biglietti>0:
    num_biglietti_che_utente_vuole_acquistare = int(input("Inserire il numero di biglietti: "))
    if num_biglietti_che_utente_vuole_acquistare > 0 and num_biglietti_che_utente_vuole_acquistare <= max_biglietti_acquistabili_singolo_utente and num_biglietti_che_utente_vuole_acquistare <= max_biglietti:
        max_biglietti -= num_biglietti_che_utente_vuole_acquistare
        num_acquirenti += 1
        print(max_biglietti)

print(f"Numero acquirenti: {num_acquirenti}")
