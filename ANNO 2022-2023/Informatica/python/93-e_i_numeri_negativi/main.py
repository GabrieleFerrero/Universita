"""
Estendere il programma dell’esercizio 09.1.3 affinché funzioni
correttamente anche con sequenze che possono contenere numeri negativi.
"""


MAX_ASTERISCHI = 40

def acquisisci_lista(frase):
    lista = []
    print(frase)
    while True:
        num = input("Inserisci numero: ")
        if num == "": break
        else: lista.append(int(num))

    return lista


lista = acquisisci_lista("")

lista_abs = [abs(el) for el in lista]
numero_massimo = max(lista_abs)

for el in lista:
    # asterischi : numero_da_rappresentare = MAX_ASTERISCHI : numero_massimo
    if el<0:
        num_asterischi = int((abs(el)*MAX_ASTERISCHI/numero_massimo))
        print(" "*(MAX_ASTERISCHI-num_asterischi),"*"*num_asterischi)
    else:
        print(" "*MAX_ASTERISCHI,"*" * int((el * MAX_ASTERISCHI / numero_massimo)))


