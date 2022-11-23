"""
Scrivere un programma che giochi a tris. Il gioco del tris si svolge su una griglia
3 × 3. Il gioco è giocato da due giocatori umani che si alternano. Il primo giocatore segna le mosse
con un cerchio ('o'), il secondo con una croce ('x'). Vince il giocatore che ha formato una
sequenza orizzontale, verticale o diagonale di 3 segni. Il programma deve, ad ogni turno,
visualizzare il tabellone di gioco, chiedere in input all'utente le coordinate del prossimo segno (riga e
colonna, numerate da 1 a 3), invertire i giocatori dopo ogni mossa e, finita la partita, decretare il
vincitore o la condizione di parità.
"""

def verifica_pareggio(campo):
    if "-" not in [cella for riga in campo for cella in riga]: return True

def verifica_vittoria(campo, giocatore):
    n = 3

    # controllo per righe
    for riga in campo:
        if riga[0] == giocatore and riga[1] == giocatore and riga[2] == giocatore: return True

    # controllo per colonna
    for i in range(n):
        if campo[0][i] == giocatore and campo[1][i] == giocatore and campo[2][i] == giocatore: return True

    # controllo per diagonali
    if campo[0][0] == giocatore and campo[1][1] == giocatore and campo[2][2] == giocatore: return True
    if campo[0][2] == giocatore and campo[1][1] == giocatore and campo[2][0] == giocatore: return True

    return False


def print_campo(campo):

    print("_"*13)

    for y in range(3):
        riga = ""
        for x in range(3):
            riga += "| "
            if campo[y][x] == "-": riga += "  "
            else: riga += campo[y][x]+" "
            if x==3-1: riga += "|\n"
        print(riga, end="")
        if y != 3-1:
            print("|---|---|---|")
    print("¯" * 13)


def chiedi_input(campo, giocatore):
    def is_int(stringa):
        try:
            _ = int(stringa)
            return True
        except:
            return False


    while True:
        scelta = input(f"È il turno di {giocatore}\nInserire la posizione [y,x]: ")
        if len(scelta.split(",")) == 2:
            scelta = scelta.split(",")
            if is_int(scelta[0]) and is_int(scelta[1]):
                y = int(scelta[0])
                x = int(scelta[1])
                if 1 <= x <= 3 and 1<= y <= 3:
                    if campo[y-1][x-1] == "-":
                        return [y-1,x-1]


def cambia_turno(giocatore):
    if giocatore=="X": return "O"
    if giocatore=="O": return "X"



def main():
    campo = [["-"]*3 for _ in range(3)]
    turno_giocatore = "X"
    while True:
        print_campo(campo)
        scelta = chiedi_input(campo, turno_giocatore)
        campo[scelta[0]][scelta[1]] = turno_giocatore
        if verifica_vittoria(campo, turno_giocatore):
            print_campo(campo)
            print(f"Ha vinto giocatore {turno_giocatore}")
            break
        else:
            if verifica_pareggio(campo):
                print_campo(campo)
                print("Pareggio")
                break

        turno_giocatore = cambia_turno(turno_giocatore)


main()
