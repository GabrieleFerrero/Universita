"""
Scrivere la funzione:
def count_vowels(string)
che restituisca il numero di vocali presenti nella stringa string. Le vocali sono le lettere a, e, i, o e
u, oltre alle rispettive versioni maiuscole.
"""

def count_vowels(stringa):
    stringa = stringa.lower()
    return stringa.count("a")+stringa.count("e")+stringa.count("i")+stringa.count("o")+stringa.count("u")


stringa = input("Inserire stringa: ")
print(count_vowels(stringa))

