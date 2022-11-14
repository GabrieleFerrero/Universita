"""
Spesso i dati raccolti durante un esperimento vanno elaborati per
rimuovere parte del rumore di misura. Un approccio semplice a questo problema prevede di
sostituire, in una lista di valori, ciascun valore con la media tra il valore stesso e i due valori adiacenti
(o dell’unico valore adiacente se il valore in esame si trova a una delle due estremità della lista).
Scrivere un programma che svolga tale operazione, senza creare una seconda lista.
"""

def acquisisci_lista(frase):
    lista = []
    print(frase)
    while True:
        num = input("Inserisci numero: ")
        if num == "": break
        else: lista.append(int(num))

    return lista

lista = acquisisci_lista("Acquisizone lista")

for i in range(len(lista)):
    if i == 0:
        lista[i] = (lista[i]+lista[i+1])/2
    elif 0 < i < len(lista)-2:
        lista[i] = (lista[i-1]+lista[i]+lista[i+1])/3
    elif i == len(lista)-1:
        lista[i] = (lista[i]+lista[i-1])/2


print(lista)
