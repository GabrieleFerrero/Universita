"""
Scrivere un programma che memorizzi due numeri interi in due costanti definite
nel codice, e poi ne visualizzi:
A. La somma;
B. La differenza;
C. Il prodotto;
D. Il valore medio;
E. La distanza (cioè il valore assoluto della differenza);
F. Il valore massimo (cioè il maggiore tra i due);
G. Il valore minimo (cioè il minore tra i due).
"""


num1 = int(input("inserisci il primo numero: "))
num2 = int(input("inserisci il secondo numero: "))

print(f"La somma è: {num1+num2}")
print(f"La differenza è: {num1-num2}")
print(f"Il prodotto è: {num1*num2}")
print(f"Il valore medio è: {(num1+num2)/2}")
print(f"La distanza è: {abs(num1-num2)}")
print(f"Il massimo è: {num1 if num1 > num2 else num2}") # oppure print(max(num1,num2))
print(f"Il minimo è: {num1 if num1 < num2 else num2}") # oppure print(min(num1,num2))