"""
Scrivere lo pseudocodice per un algoritmo che, data una lista di lunghezza definita,
sposta gli elementi “in avanti” di una posizione (incrementando quindi il loro indice di una unità), e
sposta l’elemento all’ultima posizione nella prima posizione. Ad esempio, la lista 1 7 9 3 0 4,
dopo questa operazione, diventa la lista 4 1 7 9 3 0. Scrivere poi un programma che implementi
l’algoritmo così definito.
"""

def acquisisci_lista(frase):
    lista = []
    print(frase)
    while True:
        num = input("Inserisci numero: ")
        if num == "": break
        else: lista.append(int(num))

    return lista

lista = acquisisci_lista("")
print(lista)


def sposta_in_avanti(lista):

    num_prec = lista[0]
    for i, _ in enumerate(lista):
        num_prec_momentaneo = lista[i]
        lista[i] = num_prec
        num_prec = num_prec_momentaneo
    lista[0] = num_prec





sposta_in_avanti(lista)
print(lista)
sposta_in_avanti(lista)
print(lista)