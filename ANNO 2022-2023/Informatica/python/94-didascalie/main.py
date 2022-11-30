"""
Estendere il programma dell’esercizio 09.1.3 aggiungendo una didascalia a fianco
di ciascuna barra. Il programma deve richiedere in input all’utente sia le didascalie che i valori della
sequenza. L’output deve seguire il seguente formato
"""

MAX_ASTERISCHI = 40

def acquisisci_lista(frase):
    lista = []
    print(frase)
    while True:
        didascalia = input("Inserisci didascalia: ")
        num = input("Inserisci numero: ")

        if num == "" or didascalia == "": break
        else: lista.append([didascalia, int(num)])

    return lista


lista = acquisisci_lista("")

lista_didascalie = [el[0] for el in lista]
didascalia_massima = len(lista_didascalie[0])
for didascalia in lista_didascalie:
    if len(didascalia) > didascalia_massima:
        didascalia_massima = len(didascalia)
lista_numeri = [el[1] for el in lista]
numero_massimo = max(lista_numeri)

for el in lista:
    # asterischi : numero_da_rappresentare = MAX_ASTERISCHI : numero_massimo
    eval("""print(f"{el[0]: >LUNGHEZZA_DIDASCALIA_MASSIMAs}   ", end="")""".replace("LUNGHEZZA_DIDASCALIA_MASSIMA", f"{didascalia_massima}"))
    print("*"*int((el[1]*MAX_ASTERISCHI/numero_massimo)))


