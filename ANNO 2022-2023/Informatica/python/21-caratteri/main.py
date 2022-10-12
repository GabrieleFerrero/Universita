"""
Scrivere un programma che memorizzi una stringa in una variabile e, a partire da
quella variabile, visualizzi i primi tre caratteri della stringa, seguiti da tre punti, ancora seguiti dagli
ultimi tre caratteri.

Ad esempio, se la stringa viene inizializzata al valore “Mississippi”, il
programma deve visualizzare “Mis...ppi”. Cosa succede della stringa è più corta di 6 caratteri? E
se è più breve di 3 caratteri?
"""

stringa = input("Inserire una stringa: ")
print(f"{stringa[:3]}...{stringa[-3:]}")