"""
Scrivere una funzione remove_min(v) che rimuova il valore
minimo da una lista v senza usare la funzione min() né il metodo remove().
"""

def remove_min(v):
    min = v[0]
    index = 0

    for i, el in enumerate(v):
        if el < min:
            min = el
            index = i

    new_lista = []
    for i, el in enumerate(v):
        if i != index:
            new_lista.append(el)

    return new_lista, min, index


lista = []
while True:
    num = int(input("Inserire numero: "))
    if num < 0: break
    else: lista.append(num)

print(remove_min(lista))



