"""
Scrivere un programma che chieda all’utente un numero intero e, visualizzi in
output un messaggio che descriva se il numero è primo oppure no.
"""
import math

numero = int(input("Inserire numero: "))

numero = abs(numero)

primo = True
for n in range(2, int(math.sqrt(numero))+1):
    if numero%n==0:
        primo=False
        break

print(primo)
