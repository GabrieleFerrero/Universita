"""
Scrivere un programma che chieda all’utente un numero intero e ne
visualizzi i fattori primi. Se, ad esempio, l’utente fornisce il numero 150, il programma deve
visualizzare:
2
3
5
5
"""
import math

numero = int(input("Inserire il numero: "))
numero_primo = 2

while numero_primo<=numero:
    while True:
        primo = True
        for divisore in range(2, int(math.sqrt(numero_primo))+1):
            if numero_primo%divisore==0:
                primo=False
                break

        if primo: break
        else: numero_primo += 1

    if numero%numero_primo==0:
        numero //= numero_primo
        print(numero_primo)
    else: numero_primo += 1
