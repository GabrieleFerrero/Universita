"""
Una frase di chiusura di questa prima esercitazione, all'interno di una cornice grafica a vostra
scelta, che includa il calcolo della percentuale di esercizi che avete portato a compimento.
"""

esercizi = [True,True,True,True,True,True,True,True,True,True,True,True,True,True,True]

num_es_fatti = 0
for esercizio in esercizi:
    if esercizio: num_es_fatti += 1

nome = f"Fine prima esercitazione! {(num_es_fatti*100)/len(esercizi)}%"
print(f'+{"-"*(len(nome)+2)}+')
print(f'¦ {nome} ¦')
print(f'+{"-"*(len(nome)+2)}+')