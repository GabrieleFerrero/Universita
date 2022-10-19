"""
L’algoritmo seguente (già visto nell’esercizio 01.1.2) individua la stagione
(Spring, Summer, Fall o Winter, cioè, rispettivamente, primavera, estate, autunno o inverno) a cui
appartiene una data, fornita come mese e giorno.
Se mese è 1, 2 o 3
stagione = “Winter”
Altrimenti se mese è 4, 5 o 6
stagione = “Spring”
Altrimenti se mese è 7, 8 o 9
stagione = “Summer”
Altrimenti se mese è 10, 11 o 12
stagione = “Fall”
Se mese è divisibile per 3 e giorno >= 21
Se stagione è “Winter”
stagione = “Spring”
Altrimenti se stagione è “Spring”
stagione = “Summer”
Altrimenti se stagione è “Summer”
stagione = “Fall”
Altrimenti
stagione = “Winter”
Riprendere l’analisi dell’algoritmo e scrivere poi un programma che, implementandolo, chieda
all’utente un mese e un giorno e, poi, visualizzi la stagione determinata da questo algoritmo,
verificandone la correttezza.
"""

mese = int(input("Inserire mese: "))
giorno = int(input("Inserire giorno: "))
stagione = ""

if mese==1 or mese==2 or mese == 3:
    stagione = "Winter"
elif mese==4 or mese==5 or mese == 6:
    stagione = "Spring"
elif mese==7 or mese==8 or mese == 9:
    stagione = "Summer"
elif mese==10 or mese==11 or mese == 12:
    stagione = "Fall"

if mese%3==0 and giorno >= 21:
    if stagione == "Winter":
        stagione = "Spring"
    elif stagione == "Spring":
        stagione = "Summer"
    elif stagione == "Summer":
        stagione = "Fall"
    else:
        stagione = "Winter"

print(stagione)