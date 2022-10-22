"""
Scrivere un programma che legge una sequenza di numeri interi (la
sequenza termina quando viene inserita una stringa vuota) e che, dopo ogni nuova acquisizione,
calcoli e visualizzi solamente i numeri adiacenti duplicati.
Se, ad esempio, i valori in ingresso al punto IV sono 1 3 3 4 5 5 6 6 6 3, il programma
visualizzerà i numeri adiacenti ripetuti almeno due volte, al termine della sequenza di numeri uguali,
quindi al momento dell’acquisizione del primo numero diverso:
I. alla prima acquisizione (1), nulla, perché il valore considerato è solo uno;
II. alla seconda acquisizione (3), nulla, perché i due valori adiacenti considerati (1 e 3) non sono
duplicati, cioè uguali tra loro;
III. alla terza acquisizione (3), ancora nulla, perché il valore acquisito è il duplicato del valore
precedente, dunque la sequenza di numeri adiacenti duplicati è iniziata, ma non è detto che
sia terminata;
IV. alla quarta acquisizione (4), il valore 3, in quanto i due valori adiacenti considerati (3 e 4)
non sono duplicati; pertanto, la sequenza di numeri adiacenti duplicati è terminata, e il
programma deve visualizzare il numero duplicato.
Secondo questa logica, se i valori acquisiti sono 1 3 3 4 5 5 6 6 6 3, il programma visualizzerà,
al termine delle sequenze di acquisizioni che rilevano duplicati adiacenti, dunque alla prima
acquisizione di un numero diverso: 3 5 6.
"""

numeri = []

while True:
    numero = input("Inserire numero: ")
    if numero == "": break

    numero = int(numero)

    if len(numeri)>=2:
        if numeri[-1]!=numero:
            if numeri[-2] == numeri[-1]:
                print(numeri[-1])

    numeri.append(numero)


