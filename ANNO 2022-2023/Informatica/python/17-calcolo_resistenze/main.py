"""
Scrivere un programma che, a partire dalle resistenze dei tre resistori, immesse in input dall’utente,
calcoli la resistenza totale, utilizzando la legge di Ohm.
"""

res1 = float(input("inserire valore resistenza 1: "))
res2 = float(input("inserire valore resistenza 2: "))
res3 = float(input("inserire valore resistenza 3: "))

res23 = ((1/res2) + (1/res3))**-1
res_totale = res23 + res1

print(res_totale)