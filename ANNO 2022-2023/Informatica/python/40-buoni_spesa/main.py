"""
Un supermercato premia i propri clienti con buoni spesa il cui importo dipende
dalla quantità di denaro spesa in prodotti alimentari. Ad esempio, spendendo 50 $, si ottiene un
buono spesa di importo pari all’8% di quella somma. La tabella seguente mostra la percentuale usata
per calcolare il buono spesa relativo a somme diverse. Scrivere un programma che calcoli e visualizzi
il valore del buono spesa consegnato al cliente, sulla base della somma di denaro che ha speso
nell’acquisto di prodotti alimentari.
"""

denaro_speso = float(input("Inserisci il denaro speso: "))

buono = 0
if denaro_speso < 10: buono = 0
elif denaro_speso >=10 and denaro_speso < 60: buono = denaro_speso*8/100
elif denaro_speso >=60 and denaro_speso < 150: buono = denaro_speso*10/100
elif denaro_speso >=150 and denaro_speso < 210: buono = denaro_speso*12/100
else: buono = denaro_speso*14/100

print(buono)