"""
Scrivere la funzione same_set(a, b) che verifichi se due liste
contengono gli stessi elementi, indipendentemente dall’ordine e ignorando la presenza di duplicati.
Ad esempio, le due liste 1 4 9 16 9 7 4 9 11 e 11 11 7 9 16 4 1 devono essere
considerate uguali. La funzione non deve modificare le liste che sono state passate come parametri.
"""


def acquisisci_lista(frase):
    lista = []
    print(frase)
    while True:
        num = input("Inserisci numero: ")
        if num == "": break
        else: lista.append(int(num))

    return lista

def semplifica_e_riordina(lista):
    new_lista = []
    for num in lista:
        if num not in new_lista: new_lista.append(num)
    return sorted(new_lista)

def same_set(a,b):
    return semplifica_e_riordina(a)==semplifica_e_riordina(b)


lista1 = acquisisci_lista("Acquisizione lista 1")
lista2 = acquisisci_lista("Acquisizione lista 2")

print(lista1)
print(lista2)
print(same_set(lista1,lista2))
print(lista1)
print(lista2)
