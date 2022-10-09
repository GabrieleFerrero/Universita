"""
Il quarto elemento della sequenza di Fibonacci, dove ciascun elemento ammonta alla somma
dei due precedenti.
"""

serie_fibonacci = [1,1]
lunghezza_serie_fibonacci = 10
for i in range(lunghezza_serie_fibonacci):
    if i < lunghezza_serie_fibonacci-1:
        serie_fibonacci.append(serie_fibonacci[i]+serie_fibonacci[i+1])

print(serie_fibonacci)
print(serie_fibonacci[4-1])
