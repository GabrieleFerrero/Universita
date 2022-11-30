"""
La mappa dei posti a teatro è rappresentata da una tabella con i prezzi dei biglietti
per ciascun posto, come questa.
10, 10, 10, 10, 10, 10, 10, 10, 10, 10
10, 10, 10, 10, 10, 10, 10, 10, 10, 10
10, 10, 10, 10, 10, 10, 10, 10, 10, 10
10, 10, 20, 20, 20, 20, 20, 20, 10, 10
10, 10, 20, 20, 20, 20, 20, 20, 10, 10
10, 10, 20, 20, 20, 20, 20, 20, 10, 10
20, 20, 30, 30, 40, 40, 30, 30, 20, 20
20, 30, 30, 40, 50, 50, 40, 30, 30, 20
30, 40, 50, 50, 50, 50, 50, 50, 40, 30
Scrivere un programma che chieda all’utente di scegliere o un posto (fornendo riga e colonna), o un
prezzo o l’uscita dal programma. Quando l’utente specifica un posto, accertarsi che sia libero e che
le coordinate siano all’interno della tabella. Quando, invece, specifica un prezzo, assegnare un posto
qualsiasi tra quelli disponibili a quel prezzo (se ve ne sono). Contrassegnare con un prezzo uguale a
0 i posti già venduti.
"""


def print_posti(posti):
    for riga in posti:
        print(riga)

posti = [
    [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
    [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
    [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
    [10, 10, 20, 20, 20, 20, 20, 20, 10, 10],
    [10, 10, 20, 20, 20, 20, 20, 20, 10, 10],
    [10, 10, 20, 20, 20, 20, 20, 20, 10, 10],
    [20, 20, 30, 30, 40, 40, 30, 30, 20, 20],
    [20, 30, 30, 40, 50, 50, 40, 30, 30, 20],
    [30, 40, 50, 50, 50, 50, 50, 50, 40, 30]
]

print_posti(posti)

while True:
    scelta = input("Inserire opzione [x:y o prezzo o exit]: ")

    if scelta=="exit": break
    elif ":" in scelta:
        x = int(scelta.split(":")[0])
        y = int(scelta.split(":")[1])

        if posti[y][x] != 0:
            posti[y][x] = 0
            print(f"Devi pagare {posti[y][x]}")
        else: print("Il posto non è libero")

    else:
        trovato = False

        if int(scelta) != 0:
            for y in range(len(posti)):
                for x in range(len(posti[y])):
                    if posti[y][x] == int(scelta):
                        trovato = True
                        posti[y][x] = 0
                        break
                if trovato: break

        if trovato == False:
            print("Posto con quel prezzo non disponibile")

    print_posti(posti)





