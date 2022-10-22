"""
Scrivere un programma che legga una parola e visualizzi tutte le sue
sottostringhe, ordinate per lunghezza crescente. Se, ad esempio, l’utente fornisce la stringa 'rum', il
programma deve visualizzare:
r
u
m
ru
um
rum
"""

stringa = input("Inserire la stringa: ")

for len_sottostrighe in range(1, len(stringa)+1):
    for i in range(0, len(stringa)):
        if len(stringa[i:i+len_sottostrighe]) >= len_sottostrighe:
            print(stringa[i:i+len_sottostrighe])