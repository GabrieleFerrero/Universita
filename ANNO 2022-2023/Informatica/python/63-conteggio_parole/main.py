"""
Scrivere la funzione:
def count_words(string)
che restituisca il numero di parole presenti nella stringa string. Le parole sono sequenze di
caratteri separate da spazi (si ipotizzi che tra due parole consecutive vi sia esattamente uno spazio).
Ad esempio, count_words("Mary had a little lamb") restituisce 5.
Come si potrebbe estendere l’esercizio in modo da trattare correttamente delle stringhe in cui siano
presenti più spazi tra le parole?
"""

def count_words(stringa):
    count = 0
    for parola in stringa.split(" "):
        if parola != "":
            count += 1

    return count


stringa = input("Inserire la stringa: ")
print(count_words(stringa))