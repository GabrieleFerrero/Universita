"""
Scrivere una funzione che calcoli il saldo di un conto bancario accreditando gli
interessi annualmente. La funzione riceve come parametri il numero di anni, il saldo iniziale e il tasso
d’interesse annuo.
"""

def calcolo_saldo(saldo_iniziale, tasso_interesse, numero_anni):
    saldo_finale = saldo_iniziale

    for _ in range(1, numero_anni):
        saldo_finale += (saldo_finale*(tasso_interesse/100))

    return saldo_finale



saldo_iniziale = float(input("Inserire il saldo iniziale: "))
tasso_interesse = float(input("Inserire il tasso di interesse: "))
numero_anni = int(input("Inserire il numero di anni: "))

print(calcolo_saldo(saldo_iniziale, tasso_interesse, numero_anni))