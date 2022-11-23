"""
Scrivere la funzione merge_sorted(a, b) che unisca due liste
(che si assumono già ordinate in modo crescente), restituendo una nuova lista ordinata in modo
crescente. Gestire un indice corrente per ciascuna lista, in modo da tenere traccia delle porzioni già
elaborate. Le liste di partenza non devono essere modificate. Se, ad esempio, il contenuto di a è 1
4 9 16 e il contenuto di b è 4 7 9 9 11, l’invocazione merge_sorted(a, b) restituisce
una nuova lista contenente i valori 1 4 4 7 9 9 9 11 16. Non utilizzare il metodo sort() né
la funzione sorted().
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

def sorted_list(a):
    new_a = a.copy()

    while True:
        fine = True
        for i in range(len(new_a)):
            if i < len(new_a)-1:
                if new_a[i] > new_a[i+1]:
                    new_a[i], new_a[i+1] = new_a[i+1], new_a[i]
                    fine = False

        if fine: break

    return new_a


def merge_sorted(a,b):
    return sorted_list(merge(a, b))

lista1 = acquisisci_lista("")
lista2 = acquisisci_lista("")


print(lista1)
print(lista2)

print(merge_sorted(lista1,lista2))
