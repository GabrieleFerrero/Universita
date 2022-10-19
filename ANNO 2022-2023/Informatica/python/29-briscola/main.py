"""
Si scriva un programma Python che permetta di valutare il vincitore di una mano
di una partita a Briscola tra due giocatori.

Ipotizziamo che il programma decida automaticamente (in modo casuale) il "seme di briscola", e lo
stampi come informazione iniziale. Il seme è codificato da una delle lettere C, Q, F, P.

I due utenti inseriscono poi ciascuno la carta giocata, sotto forma di stringa, che contiene
il valore seguito dal seme. I valori delle carte sono: A 2 3 4 5 6 7 J Q K. Il valore delle carte
è crescente, con l'eccezione del 3 (che viene dopo il K) e dell'A (che vien dopo il 3).

Il primo giocatore gioca una carta, il cui seme definisce il seme della mano di gioco.
Il secondo giocatore può giocare una carta di un seme diverso (e quindi perde), oppure
una carta dello stesso seme (ed in tal caso vincerà colui che ha giocato la carta più alta).
Eccezione: le carte il cui seme è pari al "seme di briscola" vincono sempre sulle carte di ogni altro seme.

Il programma, dopo avere stampato il seme di briscola scelto, accetterà la giocata del primo giocatore e del
secondo giocatore. Ogni giocata sarà quindi una stringa di due caratteri (es.: 3Q, JF, ...).
Il programma accetterà sia lettere maiuscole che minuscole, e verificherà la correttezza del dato immesso.

Se i dati immessi sono corretti, il programma determinerà il vincitore della mano, stampando "Vince
giocatore 1" oppure "Vince giocatore 2".
"""

import random


def verifica_carta(carta):
    if carta[0] in numeri_ammessi and carta[1] in semi_ammessi: return True
    return False

numeri_ammessi = {"A":12,"2":2,"3":11,"4":4,"5":5,"6":6,"7":7,"J":8,"Q":9,"K":10}
# in realtà il dizionario sarebbe: {"A":11,"2":2,"3":10,"4":4,"5":5,"6":6,"7":7,"J":2,"Q":3,"K":4} ma noi dobbiamo solo calcolare chi ha la carta maggiore e non il PUNTEGGIO
semi_ammessi = ["F","Q","P","C"]

seme_estratto = random.choice(semi_ammessi)

print(f"Seme estratto: {seme_estratto}")

carta_giocatore_1 = input("Carta giocatore 1: ")
carta_giocatore_2 = input("Carta giocatore 2: ")

carta_giocatore_1 = carta_giocatore_1.upper().strip()
carta_giocatore_2 = carta_giocatore_2.upper().strip()

# VERIFICA CARTE CORRETTE
if not(verifica_carta(carta_giocatore_1) and verifica_carta(carta_giocatore_2)): exit("Carte inserite errate")
if (carta_giocatore_1[0] == carta_giocatore_2[0]) and (carta_giocatore_1[1] == carta_giocatore_2[1]): exit("Carte inserite errate")

# VERIFICA VITTORIA
if carta_giocatore_1[1]==seme_estratto and carta_giocatore_2[1]!=seme_estratto: print("Vittoria giocatore 1")
elif carta_giocatore_1[1]!=seme_estratto and carta_giocatore_2[1]==seme_estratto: print("Vittoria giocatore 2")
elif carta_giocatore_1[1] != carta_giocatore_2[1]: print("Vittoria giocatore 1")
else:
    if numeri_ammessi[carta_giocatore_1[0]] > numeri_ammessi[carta_giocatore_2[0]]: print("Vittoria giocatore 1")
    else: print("Vittoria giocatore 2")