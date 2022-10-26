"""
Una persona ubriaca si trova in una griglia di strade. A ciascun incrocio,
sceglie a caso una delle quattro direzioni, cammina fino all’incrocio successivo, e ripete la stessa
scelta casuale. Si potrebbe pensare che, nel complesso, la persona non si sposterà di molto, perché
nel complesso gli spostamenti legati a queste scelte casuali si annulleranno a vicenda. Ma le cose
stanno davvero così? Scrivere un programma che rappresenti le posizioni sulla griglia di strade come
coppie di interi (𝑥, 𝑦). Implementare la camminata della persona ubriaca considerando 100 incroci
e (0, 0) come posizione di partenza.
"""


import random

direzioni = ["U", "D", "L", "R"]
pos = [0, 0] # x,y

print(f"Posizione iniziale: {pos}")

for _ in range(100):
    direzione = random.choice(direzioni)
    if direzione == "U": pos[1] += 1
    elif direzione == "D": pos[1] -= 1
    elif direzione == "R": pos[0] += 1
    elif direzione == "L": pos[0] -= 1

    print(f"Direzione: {direzione}\tPosizione intermedia: {pos}")

print(f"Posizione finale: {pos}")