"""
Scrivere una funzione merge(a, b) che unisca le due liste a e b,
alternando un elemento della prima e un elemento della seconda. Se una lista è più corta dell’altra,
gli elementi vengono alternati fin quando è possibile, poi gli elementi rimasti nella lista più lunga
vengono aggiunti, in ordine, in fondo. Le liste di partenza non devono essere modificate. Se, ad
esempio, il contenuto di a è 1 4 9 16 e il contenuto di b è 9 7 4 9 11, l’invocazione di
merge(a, b) restituisce una nuova lista contenente i valori 1 9 4 7 9 4 16 9 11.
"""

def acquisisci_lista(frase):
    lista = []
    print(frase)
    while True:
        num = input("Inserisci numero: ")
        if num == "": break
        else: lista.append(int(num))

    return lista


def merge(a,b):
    new_lista = []

    if len(a)>len(b): resto = a[len(b):len(a)]
    else: resto = b[len(a):len(b)]

    for el_a, el_b in zip(a,b):
        new_lista.append(el_a)
        new_lista.append(el_b)

    for el_r in resto:
        new_lista.append(el_r)

    return new_lista



lista1 = acquisisci_lista("")
lista2 = acquisisci_lista("")

print(merge(lista1,lista2))

