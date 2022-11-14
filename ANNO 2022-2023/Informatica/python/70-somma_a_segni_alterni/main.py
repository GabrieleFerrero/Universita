"""
Scrivere un programma che riceva in input una sequenza di numeri
interi (terminata da una riga vuota), e che calcoli la somma alternata dei suoi elementi. Ad esempio,
se il programma legge i dati 1 4 9 16 9 7 4 9 11, deve calcolare e visualizzare 1 – 4 + 9 –
16 + 9 – 7 + 4 – 9 + 11 = –2.
"""

numeri = []
while True:
    num = int(input("Inserire il numero: "))
    if num < 0: break
    else: numeri.append(num)

segno = 1
somma = 0
for num in numeri:
    print(f"{'-' if segno == -1 else '+'} {num} ", end="")
    somma += num*segno

    if segno == -1: segno = 1
    else: segno = -1

print(f"= {somma}")

