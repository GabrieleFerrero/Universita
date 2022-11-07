"""
Un’organizzazione non governativa ha bisogno di un programma per calcolare la quota
di sussidio economico da assegnare a ciascuna famiglia bisognosa di assistenza. La formula è la
seguente:
I. Se il reddito annuo della famiglia è compreso tra $ 30000 e $ 40000 e la famiglia ha
almeno 3 figli, il sussidio è pari a $ 1000 per ogni figlio;
II. Se il reddito annuo della famiglia è compreso tra $ 20000 e $ 30000 e la famiglia ha
almeno 2 figli, il sussidio è pari a $ 1500 per ogni figlio;
III. Se il reddito annuo della famiglia è minore di $ 20000, il sussidio è pari a $ 2000 per
ogni figlio.
Scrivere una funzione che faccia questi calcoli. Poi scrivere un programma che, in un ciclo, chieda
all’utente di fornire il reddito annuo e il numero di figli di ciascuna famiglia richiedente il sussidio,
visualizzando il corrispondente valore restituito dalla funzione. Usate –1 come valore sentinella per
terminare l’immissione dei dati.
"""


def calcolo_sussidio(reddito, numero_figli):

    sussidio = 0

    if 30000 < reddito <= 40000:
        if numero_figli >= 3:
            sussidio = 1000*numero_figli
    elif 20000 < reddito <= 30000:
        if numero_figli >= 2:
            sussidio = 1500*numero_figli
    elif 0 < reddito <= 20000:
        sussidio = 2000*numero_figli

    return sussidio

while True:
    reddito = float(input("Inserire il reddito: "))
    if reddito==-1:break
    numero_figli = int(input("Inserire il numero di figli: "))
    if numero_figli==-1: break

    print(calcolo_sussidio(reddito,numero_figli))



