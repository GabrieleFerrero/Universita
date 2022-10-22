"""
Scrivere un programma che legge una sequenza di numeri interi (la sequenza
termina quando viene inserita una stringa vuota) e che, dopo ogni nuova acquisizione, calcoli e
visualizzi:
I. le somme parziali di tutti i numeri acquisiti; Il programma deve visualizzare il risultato dei
calcoli dopo ogni nuova acquisizione.
Se, ad esempio, i valori in ingresso sono 1 7 2 9, il programma visualizzerà la somma
parziale dei numeri acquisiti dopo ogni acquisizione:
a. alla prima acquisizione (1), il primo valore acquisito: 1;
b. alla seconda acquisizione (7), la somma tra la prima e la seconda acquisizione: 1 +
7 = 8;
c. alla terza acquisizione (2), la somma tra la prima, la seconda e la terza acquisizione:
1 + 7 + 2 = 10;
d. alla quarta acquisizione (9), la somma tra la prima, la seconda, la terza e la quarta
acquisizione: 1 + 7 + 2 + 9 = 19.
II. il valore minimo e il valore massimo tra quelli acquisiti;
III. il numero di valori pari e il numero di valori dispari tra quelli acquisiti.
"""

somma = 0
numeri = []
while True:
    numero = input("Inserire il numero intero: ")
    if numero == "": break
    somma+= int(numero)
    numeri.append(int(numero))
    print(somma)

print(f"Massimo {max(numeri)}")
print(f"Minimo {min(numeri)}")

n_pari = 0
n_dispari = 0

for num in numeri:
    if num%2==0: n_pari += 1
    else: n_dispari += 1

print(f"Pari {n_pari}")
print(f"Dispari {n_dispari}")