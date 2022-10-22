"""
Scrivere un programma che legga una riga di testo in ingresso sotto
forma di stringa e visualizzi quanto segue:
I. le sole lettere maiuscole della stringa;
II. le lettere in posizioni pari nella stringa;
III. la stessa stringa in cui, al posto delle vocali (maiuscole o minuscole), vi sia un underscore (_);
IV. il numero di cifre numeriche presenti nella stringa;
V. le posizioni di tutte le vocali presenti nella stringa.
"""
import string

lettere_maiuscole = list(string.ascii_uppercase)

riga = input("Inserire la riga: ")

print("le sole lettere maiuscole della stringa")
for lettera in riga:
    if lettera in lettere_maiuscole: print(lettera)

print("le lettere in posizioni pari nella stringa")
for i in range(0,len(riga),2):
    print(riga[i])

print("la stessa stringa in cui, al posto delle vocali (maiuscole o minuscole), vi sia un underscore (_)")
new_riga = riga
for lettera in "aeiouAEIOU":
    new_riga = new_riga.replace(lettera,"_")
print(new_riga)

print("il numero di cifre numeriche presenti nella stringa")
numero_cifre = 0
for cifra in "0123456789":
    numero_cifre += riga.count(cifra)
print(numero_cifre)

print("le posizioni di tutte le vocali presenti nella stringa")
pos_vocali = []
for i, lettera in enumerate(riga):
    if lettera in "aeiouAEIOU": pos_vocali.append(i)

print(pos_vocali)
