"""
Scrivere un programma che acquisisca dall’utente un elenco di
numeri interi positivi forniti su un’unica riga e separati dal carattere ':', ad esempio:
3:12:21:8:4:7. Il programma deve stampare, mantenendo lo stesso formato:
I. i numeri inseriti, esclusi il minimo e il massimo (ad esempio, 12:8:4:7);
II. tra i numeri inseriti, i soli numeri pari (ad esempio, 12:8:4);
III. tra i numeri inseriti, i soli numeri di 2 cifre (ad esempio, 12:21).
"""

def print_lista(lista):
    for i in range(len(lista)-1):
        print(f"{lista[i]}:", end="")
    print(lista[-1])


numeri = input("Inserire numeri: ")

lista_numeri = [int(el) for el in numeri.split(":")]

min = lista_numeri[0]
max = lista_numeri[0]

for el in lista_numeri:
    if el < min: min = el
    if el > max: max = el


lista_senza_max_e_min = []
for el in lista_numeri:
    if el != min and el != max: lista_senza_max_e_min.append(el)
print_lista(lista_senza_max_e_min)


lista_numeri_pari = []
for el in lista_numeri:
    if el%2==0: lista_numeri_pari.append(el)
print_lista(lista_numeri_pari)


lista_numeri_due_cifre = []
for el in lista_numeri:
    if len(str(el))==2: lista_numeri_due_cifre.append(el)
print_lista(lista_numeri_due_cifre)