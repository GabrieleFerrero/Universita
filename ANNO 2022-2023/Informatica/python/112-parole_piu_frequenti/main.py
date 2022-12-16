"""
Estendere il programma dell’esercizio 11.1.1 in modo che visualizzi
solamente le 5 parole più frequenti nel file, senza considerare nel conteggio articoli, preposizioni e
congiunzioni.
"""


nome_file = input("Inserire nome file: ")

parole_da_non_considerare = ["di","a","da","in","con","su","per","tra","fra","i","il","gli","le","la","lo","un","una","uno","e","che","ma"]

conteggio_parole = {}
with open(nome_file, "r") as file:
    for line in file:
        for parola in line.split():
            if parola not in parole_da_non_considerare:
                if parola in conteggio_parole: conteggio_parole[parola] += 1
                else: conteggio_parole[parola] = 1


def estrai_valore(chiave):
    return conteggio_parole[chiave]

lista_parole_piu_frequenti = sorted(conteggio_parole, key=estrai_valore, reverse=True)[0:5]
for parola in lista_parole_piu_frequenti:
    print(parola, conteggio_parole[parola])




