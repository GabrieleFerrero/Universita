"""
Scrivere un programma che legga una stringa e visualizzi i messaggi
appropriati, dopo aver verificato se:
I. contiene soltanto lettere;
II. contiene soltanto lettere maiuscole;
III. contiene soltanto lettere minuscole;
IV. contiene soltanto cifre numeriche decimali;
V. contiene soltanto lettere e cifre;
VI. inizia con una lettera maiuscola;
VII. termina con un punto.
"""

import re
from string import ascii_lowercase


stringa = input("Inserire la stringa: ")

presenza_lettere_minuscole = re.findall("[a-z]", stringa) # alternativa stringa.islower()
presenza_lettere_maiuscole = re.findall("[A-Z]", stringa) # alternativa stringa.isupper()

if len(presenza_lettere_maiuscole)+len(presenza_lettere_minuscole) == len(stringa): print("Contiene soltanto lettere") # alternativa stringa.isalpha()
if len(presenza_lettere_maiuscole) == len(stringa): print("Contiene soltanto lettere maiuscole")
if len(presenza_lettere_minuscole) == len(stringa): print("Contiene soltanto lettere minuscole")

presenza_numeri = re.findall("[0-9]", stringa)
if len(presenza_numeri) == len(stringa): print("Contiene soltanto numeri")

if len(presenza_numeri)+len(presenza_lettere_maiuscole)+len(presenza_lettere_minuscole) == len(stringa) and (len(presenza_lettere_minuscole)!=0 or len(presenza_lettere_maiuscole)!=0) and len(presenza_numeri)!=0: print("Contiene soltanto numeri e lettere")

if stringa[0] in ascii_lowercase.upper(): print("Inizia con una lettera maiuscola")
if stringa[-1]==".": print("Termina con un punto")