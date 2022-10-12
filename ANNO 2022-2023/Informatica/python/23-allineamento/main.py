"""
Formattare l’output dell’esercizio 02.1.1 in modo che descrizioni e numeri
siano allineati verticalmente, ad esempio:

Somma:      45
Differenza: -5
... ...
"""

num1 = int(input("inserisci il primo numero: "))
num2 = int(input("inserisci il secondo numero: "))

ris = {
    "somma":num1+num2,
    "differenza":num1-num2,
    "prodotto":num1*num2,
    "media":(num1+num2)/2,
    "distanza":abs(num1-num2),
    "massimo":max(num1,num2),
    "minimo":min(num1,num2)
}

lunghezza_riga = 50
lunghezza_massima_tra_operazione_e_numero = 15
print(f"+{'-'*lunghezza_riga}+")
for operazione, calcolo in ris.items():
    riga = f"¦ {operazione}:{' '*(lunghezza_massima_tra_operazione_e_numero-len(operazione))}{calcolo}"
    print(f"{riga}{' '*(lunghezza_riga-len(riga))} ¦")

print(f"+{'-' * lunghezza_riga}+")