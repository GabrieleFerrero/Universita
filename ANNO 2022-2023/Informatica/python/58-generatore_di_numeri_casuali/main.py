"""
Usando la formula ππππ€ = (π Γ ππππ + π) % π, in cui π , π ,
π ed π sono numeri interi, e poi ripetendo il calcolo assegnando il valore corrente di ππππ€ ad ππππ, si
ottiene un semplice generatore di numeri casuali. Scrivere un programma che chieda allβutente di
fornire un valore iniziale per ππππ (questo valore Γ¨ il seed del generatore di numeri casuali), e poi
visualizzi i primi 100 numeri interi generati, usando a = 32310901, b = 1729 e m = 224.
"""

r = 0
a = 32310901
b = 1729
m = 224

r = int(input("Inserire il seme: "))

for _ in range(100):
    r = ((a*r)+b)%m
    print(r)
