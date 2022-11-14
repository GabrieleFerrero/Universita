"""
Scrivere la funzione sum_without_smallest(v) che calcoli la
somma di tutti i valori di una lista v, escludendo il valore minimo.
"""

def acquisisci_lista(frase):
    lista = []
    print(frase)
    while True:
        num = input("Inserisci numero: ")
        if num == "": break
        else: lista.append(int(num))

    return lista

def sum_without_smallest(v):
    min = v[0]
    for num in v:
        if num < min: min = num

    somma = 0
    for num in v:
        if num != min: somma += num

    return somma


print(sum_without_smallest(acquisisci_lista("Acquisizione lista")))