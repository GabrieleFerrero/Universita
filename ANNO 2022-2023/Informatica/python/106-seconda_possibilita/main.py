"""
Scrivere un programma che chiede all’utente di inserire una serie di
valori di tipo float. Quando l’utente inserisce un valore che non è del tipo corretto, il programma
deve fornire all’utente una seconda possibilità di inserire il valore, e dopo due possibilità deve
interrompere la lettura dell’input, terminando immediatamente il programma. L’inserimento dei dati
continua finché l’utente inserisce in input una stringa vuota (''). Sommare tutti i valori
correttamente specificati e visualizzare la loro somma quando l’utente ha finito di inserire i dati.
Utilizzare la gestione delle eccezioni per rilevare gli input impropri.
"""

def is_float(number):
    try:
        _ = float(number)
        return True
    except: return False


errore = False
numeri = []
while True:
    number = input("Inserire numero: ")
    if number == "":
        break
    if not is_float(number):
        if errore: exit("Tipo non corretto\nExit...")
        else:
            errore = True
            print("Tipo non corretto")
    else:
        numeri.append(float(number))

print(sum(numeri))


