"""
Scrivere un programma 'censore', che legga un file (bad_words.txt) contenente
una lista di 'parolacce' (come 'sesso', 'droga', 'C++' e così via), una per riga, inserendole in
un insieme. Leggere poi un altro file di testo (raw_text.txt), che contenga occorrenze di alcune
delle 'parolacce' in questione. Il programma deve riscrivere il secondo file, generandone un terzo
(censored_text.txt) nel quale il contenuto sia lo stesso, ma con la differenza che tutte le
occorrenze di parole e sotto-parole corrispondenti a 'parolacce' sono sostituite da un numero di
asterischi ('*') pari alla loro lunghezza.
"""

import string

parolacce = set()
with open("bad_words.txt","r") as file:
    for riga in file:
        riga = riga.replace("\n","")
        if riga != "": parolacce.add(riga.lower())
print(parolacce)


with open("raw_text.txt","r") as file_input:
    with open("censored_text.txt", "w") as file_output:
        for riga in file_input:
            riga = riga.replace("\n","")
            for parola in riga.split():
                trovata = False
                for parolaccia in parolacce:
                    if parolaccia in parola.lower():
                        file_output.write(parola.lower().replace(parolaccia, "*"*len(parolaccia)))
                        trovata = True
                        break
                if not trovata:file_output.write(parola)
                file_output.write(" ")
            file_output.write("\n")
