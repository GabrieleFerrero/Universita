"""
primi quattro elementi della sequenza di Fibonacci, in colonna.
"""

serie_fibonacci = [1,1]
lunghezza_serie_fibonacci = 10
for i in range(lunghezza_serie_fibonacci):
    if i < lunghezza_serie_fibonacci-1:
        serie_fibonacci.append(serie_fibonacci[i]+serie_fibonacci[i+1])

print(serie_fibonacci)

for num in serie_fibonacci[:4]: print(num)