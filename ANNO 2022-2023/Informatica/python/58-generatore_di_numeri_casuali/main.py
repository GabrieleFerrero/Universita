"""
Usando la formula 𝑟𝑛𝑒𝑤 = (𝑎 × 𝑟𝑜𝑙𝑑 + 𝑏) % 𝑚, in cui 𝑎 , 𝑏 ,
𝑟 ed 𝑚 sono numeri interi, e poi ripetendo il calcolo assegnando il valore corrente di 𝑟𝑛𝑒𝑤 ad 𝑟𝑜𝑙𝑑, si
ottiene un semplice generatore di numeri casuali. Scrivere un programma che chieda all’utente di
fornire un valore iniziale per 𝑟𝑜𝑙𝑑 (questo valore è il seed del generatore di numeri casuali), e poi
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
