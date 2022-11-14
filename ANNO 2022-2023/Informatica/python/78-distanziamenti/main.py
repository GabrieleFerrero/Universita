"""
Le persone che parcheggiano la propria automobile in una fila di parcheggi di
solito preferiscono massimizzare la distanza tra il posto che occupano e i posti che sono già occupati
da altri veicoli. Tendono quindi ad occupare il posto centrale della fila più lunga di posti liberi a
disposizione.
Ad esempio, si consideri la situazione in cui dieci posti sono liberi:
_ _ _ _ _ _ _ _ _ _
La prima persona che arriva occuperà, col proprio veicolo, un posto nella parte centrale della fila:
_ _ _ _ _ X _ _ _ _
La persona successiva lo posizionerà a metà della fila lasciata libera più lunga (cioè quella di sinistra):
_ _ X _ _ X _ _ _ _
Scrivere un programma che riceva in input il numero di posti auto di cui si compone la fila di
parcheggi e che, ogni volta che un nuovo posto viene occupato secondo la regola indicata, visualizzi
la fila nel formato indicato sopra. Suggerimento: utilizzare un elenco di valori booleani per indicare
se un posto auto è occupato o meno.
"""


def print_posti(posti):
    for posto in posti:
        print("_ ",end="") if posto == False else print("X ",end="")
    print()

num_posti = int(input("Numero posti: "))
posti = [False]*num_posti
print_posti(posti)

while False in posti:
    input()

    # verifico le porzioni di spazi disponibili

    porzioni_di_spazio_libere = [] # [indice_inizio, lunghezza]

    new_serie_di_posti = True
    for i, posto in enumerate(posti):
        if posto == False:
            if new_serie_di_posti:
                porzioni_di_spazio_libere.append([i, 1])
                new_serie_di_posti = False
            else:
                porzioni_di_spazio_libere[-1][1] += 1

        else: new_serie_di_posti = True

    # verifico lo spazio più grande

    index=0
    max = porzioni_di_spazio_libere[0][1]
    for i, dato in enumerate(porzioni_di_spazio_libere):
        if dato[1] > max:
            max = dato[1]
            index = i


    # inserisco l'auto

    posti[porzioni_di_spazio_libere[index][0]+int(porzioni_di_spazio_libere[index][1]/2)] = True

    print_posti(posti)
