"""
Scrivere un programma che chieda all’utente di inserire un valore N, crei una matrice
di N x N elementi, e vi inserisca una sequenza di numeri interi con valori compresi tra 1 e N**2
visualizzando poi la tabella così riempita. Ad esempio, se N = 4, il programma dovrà stampare la
tabella illustrata sulla sinistra, seguendo le direzioni illustrate nella tabella di destra (che non deve
essere visualizzata dal programma).
1  2  3  4      ⨀ → → ↴
12 13 14 5      ↱ → ↴ ↓
11 16 15 6      ↑ ⨂ ↵ ↓
10 9  8  7      ⬑ ← ← ↵
"""


def print_matrice(n, matrice):
    spazi = len(str(n ** 2))
    if spazi % 2 != 0:
        spazi += 1

    print("_" * (n * (spazi + 2 + 1) + 1))

    for y in range(n):
        riga = ""
        for x in range(n):
            riga += eval("""f'|{matrice[y][x]: ^LUNGHEZZA}' """.replace("LUNGHEZZA", str(spazi + 2)))
            if x == n - 1: riga += "|\n"
        print(riga, end="")
        if y != n - 1:
            print((("|" + ("-" * (spazi + 2))) * n) + "|")
    print("¯" * (n * (spazi + 2 + 1) + 1))
    print()


n = int(input("Inserire il valore di N: "))

matrice_numeri = [[0] * n for _ in range(n)]
matrice_segni = [[0] * n for _ in range(n)]

#print_matrice(n, matrice_numeri)
#print_matrice(n, matrice_segni)

ultimo_numero = 1
x = 0
y = 0
diminuizione_lato = 0

while True:

    esci=False
    for x in range(diminuizione_lato, n - diminuizione_lato):
        if ultimo_numero == (n ** 2):
            matrice_segni[y][x] = "⨂"
            matrice_numeri[y][x] = ultimo_numero
            esci=True
            break
        elif x == 0 and y == 0:
            matrice_segni[y][x] = "⨀"
        elif x == (n - diminuizione_lato - 1):
            matrice_segni[y][x] = "↴"
        else:
            matrice_segni[y][x] = "→"
        matrice_numeri[y][x] = ultimo_numero
        ultimo_numero += 1
    if esci: break

    esci = False
    for y in range(diminuizione_lato + 1, n - diminuizione_lato - 1):
        if ultimo_numero == (n ** 2):
            matrice_segni[y][x] = "⨂"
            matrice_numeri[y][x] = ultimo_numero
            esci=True
            break
        else:
            matrice_segni[y][x] = "↓"
        matrice_numeri[y][x] = ultimo_numero
        ultimo_numero += 1
    if esci: break
    y+=1

    esci = False
    for x in range(n - (diminuizione_lato + 1), diminuizione_lato-1, -1):
        if ultimo_numero == (n ** 2):
            matrice_segni[y][x] = "⨂"
            matrice_numeri[y][x] = ultimo_numero
            esci=True
            break
        elif x == n - (diminuizione_lato+1):
            matrice_segni[y][x] = "↵"
        elif x == diminuizione_lato:
            matrice_segni[y][x] = "⬑"
        else:
            matrice_segni[y][x] = "←"
        matrice_numeri[y][x] = ultimo_numero
        ultimo_numero += 1
    if esci: break


    esci = False
    for y in range(n - (diminuizione_lato + 2), diminuizione_lato, -1):
        if ultimo_numero == (n ** 2):
            matrice_segni[y][x] = "⨂"
            matrice_numeri[y][x] = ultimo_numero
            esci=True
            break
        elif y == diminuizione_lato + 1:
            matrice_segni[y][x] = "↱"
        else:
            matrice_segni[y][x] = "↑"
        matrice_numeri[y][x] = ultimo_numero
        ultimo_numero += 1
    if esci: break

    diminuizione_lato += 1

print_matrice(n, matrice_numeri)
print_matrice(n, matrice_segni)
