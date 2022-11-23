"""
Una matrice 𝑛 × 𝑛 contenente i numeri interi 1, 2, 3, ... , 𝑛2 è un
“quadrato magico” se la somma dei suoi elementi in ciascuna riga, in ciascuna colonna e nelle due
diagonali ha lo stesso valore. Ad esempio, questo è un quadrato magico di dimensione 4:
16 3 2 13
5 10 11 8
9 6 7 12
4 15 14 1
Scrivere un programma che acquisisca in ingresso 16 valori, li disponga in una tabella 4 × 4 in
ordine, una riga alla volta dall’alto in basso, e in ciascuna riga da sinistra a destra, e verifichi se, dopo
averli disposti, questi formano un quadrato magico. Verificare due proprietà:
I. Nei dati acquisiti sono presenti tutti e solamente i numeri 1, 2, ..., 16.
II. Quando i numeri vengono disposti nella tabella, le somme delle righe, delle colonne e delle
diagonali sono tutte uguali l’una all’altra.
"""


def verifica_numeri(quadrato):
    array = [cella for riga in quadrato for cella in riga ]
    for num in range(1,16+1):
        if num not in array: return False

    return True


def check_quadrato_magico(quadrato, n):
    # verifica se è un quadrato magico

    somma_magica = sum(quadrato[0])

    # controllo per righe
    for riga in quadrato:
        if sum(riga) != somma_magica: return False

    # controllo per colonna
    somme = [0]*n
    for y in range(n):
        for x in range(n):
            somme[x] += quadrato[y][x]

    if sum(somme) != somma_magica*n: return False


    # controllo per diagonali
    somma_diagonale_1 = 0
    somma_diagonale_2 = 0

    for i in range(n):
        somma_diagonale_1 += quadrato[i][i]
        somma_diagonale_2 += quadrato[i][n-(i+1)]

    if somma_diagonale_1 != somma_magica: return False
    if somma_diagonale_2 != somma_magica: return False

    return True


n = 4
quadrato_magico = []

for _ in range(n):
    riga_magica = []
    for _ in range(n):
        riga_magica.append(int(input("Inserire numero: ")))
    quadrato_magico.append(riga_magica)


for riga in quadrato_magico:
    print(riga)


print(check_quadrato_magico(quadrato_magico, n))
print(verifica_numeri(quadrato_magico))