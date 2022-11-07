"""
Scrivere un programma che converta un numero romano, come
MCMLXXVIII, nella sua rappresentazione decimale.
Suggerimento: per prima cosa, scrivere una funzione che restituisca il valore numerico di ciascuna
singola lettera, poi usare l’algoritmo seguente:
totale = 0
s = stringa corrispondente al numero romano
Finché s non è vuota
Se s ha lunghezza 1, oppure il valore del suo primo carattere è maggiore o uguale al valore
del suo secondo carattere
Aggiungere il valore del primo carattere di s al totale
Rimuovere il primo carattere da s
Altrimenti
differenza = valore del secondo carattere di s - valore del primo carattere di s
Aggiungere il valore di differenza al totale
Rimuovere i primi due caratteri da s
"""

dizionario_di_conversione_numeri_da_romani_a_decimali = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}


def conversione(numero_romano):
    numero_romano = numero_romano.upper().replace(" ","")[::-1]
    numero_decimale = 0

    count = 0

    while True:
        if count >= len(numero_romano): break

        if count == len(numero_romano)-1 or dizionario_di_conversione_numeri_da_romani_a_decimali[numero_romano[count+1]] >= dizionario_di_conversione_numeri_da_romani_a_decimali[numero_romano[count]]:
            numero_decimale += dizionario_di_conversione_numeri_da_romani_a_decimali[numero_romano[count]]
            count += 1
        else:
            numero_decimale += (dizionario_di_conversione_numeri_da_romani_a_decimali[numero_romano[count]] - dizionario_di_conversione_numeri_da_romani_a_decimali[numero_romano[count+1]])
            count += 2

    return numero_decimale



numero_romano = input(("Numero romano: "))
print(conversione(numero_romano))