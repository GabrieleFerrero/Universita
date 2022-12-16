"""
Il Crivello di Eratostene è un algoritmo iterativo, noto anche nell’Antica
Grecia, che calcola tutti i numeri primi minori di un numero intero 𝑛 . Ad ogni iterazione, l’algoritmo
cancella tutti i multipli del valore minimo presente nell’insieme, partendo dal valore minimo 2 e
arrivando a considerare come valore minimo √𝑛. Alla fine dell’ultima iterazione, i numeri rimasti
nell’insieme sono quelli richiesti. Definire una funzione che implementa il Crivello di Eratostene. Per
prima cosa, definire un insieme ed inserirvi tutti i numeri interi da 2 a n. Poi, eliminare
dall’insieme tutti i multipli di 2, tranne 2 (cioè 4, 6, 8, 10, 12, e così via, fino a n). Come
secondo passo, eliminare tutti i multipli di 3, tranne 3 (cioè 6, 9, 12, 15, e così via, fino a n).
Proseguire così, cancellando ogni volta i multipli del valore minimo presente nell’insieme, fino a che i
numeri rimasti nell’insieme sono quelli richiesti.
"""

import math

def elimina_multipli(lista, multiplo):
    new_lista = []
    for el in lista:
        if el%multiplo==0:
            if el == multiplo:
                new_lista.append(el)
        else: new_lista.append(el)
    return new_lista


n = int(input("Inserire n: "))

insieme_da_2_a_n = [i for i in range(2, n+1)]

i=0
while i<int(math.sqrt(n)):
    insieme_da_2_a_n = elimina_multipli(insieme_da_2_a_n, insieme_da_2_a_n[i])
    i+=1

print(insieme_da_2_a_n)




