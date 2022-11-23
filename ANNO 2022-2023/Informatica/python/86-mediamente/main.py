"""
Scrivere la funzione neighbor_average(values, row, column) che, in
una tabella values, calcoli il valore medio dei vicini di un elemento nelle otto direzioni, indicizzati
come illustrato nella figura sotto (escludendo l’elemento stesso). Se, però, l’elemento si trova su un
bordo della tabella, la media va calcolata considerando soltanto i vicini che appartengono
effettivamente alla tabella. Ad esempio, se row e column valgono entrambe 0, l'elemento ha 3
vicini.
"""

def neighbor_average(values, row, column):
    medie = []
    for y in range(row):
        medie_riga = []
        for x in range(column):

            # trovo indici giusti:

            operazione_su_indice_centrale = [
                [-1, -1],[-1,0],[-1,+1],
                [0,-1],         [0,+1],
                [+1,-1],[+1,0],[+1,+1]
            ]

            lista_indici = []
            for operazione in operazione_su_indice_centrale:
                if (y+operazione[0] >= 0 and y+operazione[0] <= row-1) and (x+operazione[1]>=0 and x+operazione[1]<=column-1):
                    lista_indici.append([y+operazione[0], x+operazione[1]])

            # calcolo medie
            media = 0
            for indice in lista_indici:
                media += values[indice[0]][indice[1]]
            media /= len(lista_indici)

            medie_riga.append(media)
        medie.append(medie_riga)

    return medie


matrice = [
    [1,2,3,5],
    [3,5,55,8],
    [2,5,1,6]
]

for riga in neighbor_average(matrice,3,4):
    print(riga)