"""
Scrivere un programma che riceva in input una sequenza di valori reali e
visualizzi un grafico a barre che li rappresenti, usando asterischi (*) per disegnare le barre. L’output
deve seguire il seguente formato:
**********************
****************************************
****************************
**************************
**************
Assumere che tutti i valori nella sequenza di input siano positivi. Come primo passo, identificare il
valore massimo. La barra che lo rappresenta deve essere composta di 40 asterischi. Le barre più
corte devono usare un numero di asterischi proporzionale a questo per rappresentare i valori
restanti.
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

numero_massimo = max(lista)

for el in lista:
    # asterischi : numero_da_rappresentare = MAX_ASTERISCHI : numero_massimo
    print("*"*int((el*MAX_ASTERISCHI/numero_massimo)))


