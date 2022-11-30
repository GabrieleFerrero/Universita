"""
Scrivere una funzione per ciascuna delle seguenti operazioni su liste di
numeri interi, e fornire un programma per collaudare (testing) ciascuna funzione. Tutte le operazioni
devono modificare la lista passata come parametro. [P6.4]
I. Scambiare tra loro il primo e l’ultimo elemento della lista.
II. Far slittare tutti gli elementi della lista di una posizione, spostando l’ultimo elemento nella
prima posizione. Ad esempio, la lista 1 4 9 16 25 deve diventare 25 1 4 9 16.
III. Sostituire con 0 tutti gli elementi di valore pari.
IV. Sostituire ciascun elemento, tranne il primo e l’ultimo, con il maggiore dei due elementi ad
esso adiacenti.
V. Eliminare l’elemento centrale della lista se questa ha dimensione dispari, altrimenti
eliminare i due elementi centrali.
VI. Spostare tutti gli elementi pari all’inizio della lista, lasciando quelli dispari in coda, e
preservando l’ordinamento relativo tra gli elementi.
VII. Restituire il secondo valore maggiore della lista.
VIII. Restituire True se e solo se la lista è ordinata in senso crescente.
IX. Restituire True se e solo se la lista contiene due elementi adiacenti duplicati.
X. Restituire True se e solo se la lista contiene elementi duplicati (non necessariamente
adiacenti).
"""

import random

def crea_lista():
    lista = [random.randint(0,100) for _ in range(random.randint(10,20))]
    print(lista)
    return lista


def scambia():
    lista = crea_lista()
    lista[0] , lista[-1] = lista[-1] , lista[0]
    print(lista)
    print("--------------------")

def sposta_in_avanti():
    lista=crea_lista()
    num_prec = lista[0]
    for i, _ in enumerate(lista):
        num_prec_momentaneo = lista[i]
        lista[i] = num_prec
        num_prec = num_prec_momentaneo
    lista[0] = num_prec
    print(lista)
    print("--------------------")

def sostituisci_numeri_pari():
    lista = crea_lista()
    for i, el in enumerate(lista):
        if el%2==0: lista[i]=0
    print(lista)
    print("--------------------")


def sostituisci_con_maggiore_adiacente():
    lista = crea_lista()
    for i in range(1,len(lista)-1):
        if lista[i-1] > lista[i+1]: lista[i] = lista[i-1]
        else: lista[i] = lista[i+1]
    print(lista)
    print("--------------------")

def eliminare_elemento_centrale():
    lista = crea_lista()
    if len(lista)%2==0:
        n = (len(lista) // 2) - 1
        lista.pop(n)
        lista.pop(n)
    else:
        lista.pop(len(lista) // 2)
    print(lista)
    print("--------------------")

def sposta_pari():
    lista = crea_lista()
    n = 0
    for i, el in enumerate(lista):
        if el%2==0:
            lista[n], lista[i] = lista[i], lista[n]
            n += 1

    print(lista)
    print("--------------------")


def trovo_secondo_maggiore():
    lista = crea_lista()

    max=lista[0]
    for el in lista:
        if el > max:
            max=el
    for i, el in enumerate(lista):
        if el == max:
            lista.pop(i)
    max=lista[0]
    for el in lista:
        if el > max:
            max=el

    print(max)
    print("--------------------")

def lista_crescente():
    lista = crea_lista()
    lista_ordinata = lista.sort()
    print(lista==lista_ordinata)
    print("--------------------")

def elementi_duplicati_adiacenti():
    lista = crea_lista()
    for i in range(1, len(lista)):
        if lista[i - 1] == lista[i]:
            print(True)
            print("--------------------")
            return

    print(False)
    print("--------------------")


def elementi_duplicati_non_adiacenti():
    lista = crea_lista()
    for i,el in enumerate(lista):
        lista.pop(i)
        if el in lista:
            print(True)
            print("--------------------")
            return

    print(False)
    print("--------------------")


scambia()
sposta_in_avanti()
sostituisci_numeri_pari()
sostituisci_con_maggiore_adiacente()
eliminare_elemento_centrale()
sposta_pari()
trovo_secondo_maggiore()
lista_crescente()
elementi_duplicati_adiacenti()
elementi_duplicati_non_adiacenti()




