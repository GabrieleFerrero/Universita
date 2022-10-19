"""
Scrivere un programma che calcoli le tasse secondo il seguente schema. Il
programma deve acquisire dall’utente il valore del reddito, e stampare le tasse dovute. Non è
richiesto di stampare i passaggi intermedi.
"""

reddito = float(input("Inserire reddito: "))
stato_civile = input("Inserire stato civile: ")

tasse = 0
if stato_civile == "coniugato":
    if reddito > 0 and reddito <= 16000: tasse = 0+(((reddito-0)*15)/100)
    elif reddito > 16000 and reddito <= 64000: tasse = 800+(((reddito-16000)*15)/100)
    elif reddito > 64000:tasse = 4400+(((reddito-64000)*25)/100)
    else: tasse = 0
else:
    if reddito > 0 and reddito <= 8000: tasse = 0+(((reddito-0)*15)/100)
    elif reddito > 8000 and reddito <= 32000: tasse = 800+(((reddito-8000)*15)/100)
    elif reddito > 32000:tasse = 4400+(((reddito-32000)*25)/100)
    else: tasse = 0

print(tasse)