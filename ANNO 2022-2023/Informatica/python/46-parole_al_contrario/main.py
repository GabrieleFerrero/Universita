"""
Scrivere un programma che legga una parola e visualizzi:
I. la parola al contrario. Se, ad esempio, l’utente fornisce la stringa 'Ciao', il programma
deve visualizzare 'oaiC' [P4.9]
II. le lettere maiuscole partendo dal fondo. Se, ad esempio, l’utente fornisce la stringa
'CiAo', il programma deve visualizzare 'AC'.
"""

import string

lettere_minuscole = string.ascii_lowercase

stringa = input("Inserire la stringa: ")

print(stringa[::-1])

new_stringa = stringa
for lettera in lettere_minuscole:
    new_stringa = new_stringa.replace(lettera,"")

print(new_stringa[::-1])



