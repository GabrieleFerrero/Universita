"""
La legge di De Morgan permette di semplificare l’applicazione dell’operatore not
ad espressioni che contengono operatori and/or. In particolare, questa legge ha due forme, una per
la negazione di espressioni in and, e una per la negazione di espressioni in or:
not (A and B) equivale a not A or not B
not (A or B) equivale a not A and not B
Considerare le espressioni seguenti, e per ciascuna di esse applicare la legge di De Morgan. Provare a
descrivere “a parole” il significato algebrico intuitivo di ciascuna delle espressioni.
Scrivere poi un programma che prende in input un numero intero x e per ciascuna delle seguenti
espressioni (che corrispondono alla negazione delle espressioni dell’esercizio 03.1.5) stampa:
l’espressione di partenza, l’espressione una volta applicata la legge di De Morgan, e il loro valore di
verità:
I. not (x > 0 and x < 100)
II. not (x > 0 or x < 100)
III. not (x > 0 or 100 < x)
IV. not (x > 0 and x < 100 or x == -1)
"""

x = int(input("Inserire numero: "))

print(f"{'not (x > 0 and x < 100): ':<50}{(not (x > 0 and x < 100)):<10}| {'not x > 0 or not x < 100:':<50}{(not x > 0 or not x < 100):<0}")
print(f"{'not (x > 0 or x < 100): ':<50}{(not (x > 0 or x < 100)):<10}| {'not x > 0 and not x < 100:':<50}{(not x > 0 and not x < 100):<0}")
print(f"{'not (x > 0 or 100 < x): ':<50}{(not (x > 0 or 100 < x)):<10}| {'not x > 0 and not 100 < x:':<50}{(not x > 0 and not 100 < x):<0}")
print(f"{'not (x > 0 and x < 100 or x == -1): ':<50}{(not (x > 0 and x < 100 or x == -1)):<10}| {'(not x>0 or not x<100) and not x==-1:':<50}{((not x>0 or not x<100) and not x==-1):<0}")