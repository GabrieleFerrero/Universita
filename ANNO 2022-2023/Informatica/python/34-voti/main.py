"""
Scrivere un programma che traduca un voto in lettere inserito dall’utente nel
corrispondente voto numerico e lo stampi. I voti in lettere sono 'A', 'B', 'C', 'D' e 'F',
eventualmente seguiti da un segno + o –. I loro valori numerici sono, nell’ordine, 4.0, 3.0, 2.0,
1.0 e 0.0. I voti 'F+' e 'F–' non esistono. Un segno + aumenta il voto numerico di 0.3, mentre
un segno – lo diminuisce della stessa quantità. Il voto 'A+' è comunque uguale a 4.0.
"""

corrispondenza = {"A":4.0, "B":3.0, "C":2.0, "D":1.0, "F":0.0}

voto = input("Inserire voto: ")


if voto[0] not in corrispondenza: exit("Errore voto inserito")
if voto[1:].count("+")+voto[1:].count("-") != len(voto[1:]): exit("Errore voto inserito")

valore_segno = 0.3
num_meno = voto.count("-")
num_piu = voto.count("+")
somma_segni = (num_piu*valore_segno) - (num_meno*valore_segno)

valore = 0
if voto[0] == "F":
    if somma_segni > valore_segno: valore = corrispondenza[voto[0]] + somma_segni
    else: valore = corrispondenza[voto[0]]
elif voto[0] == "A":
    if somma_segni < 0: valore = corrispondenza[voto[0]] + somma_segni
    else: valore = corrispondenza[voto[0]]
else:
    valore = corrispondenza[voto[0]] + somma_segni


print(f"Voto corrispondente: {valore}")
