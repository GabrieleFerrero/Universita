"""
Un negozio di animali vuole fare uno sconto ai propri clienti se comprano
uno o più animali ed almeno cinque altri prodotti. Lo sconto equivale al 20% del costo degli altri
prodotti, esclusi gli animali. Scrivere una funzione discount(prices, is_pet) che riceva
informazioni su una vendita e calcoli il valore dello sconto da applicare. Per il prodotto i-esimo,
prices[i] è il prezzo prima di applicare sconti, e is_pet[i] è una variabile booleana che
assume valore True se il prodotto i-esimo è un animale. Scrivere un programma che richiede a chi
lavora in cassa di inserire in input, per ciascun prodotto venduto, il prezzo e poi, 'Y' se il prodotto
è un animale, e 'N' se non lo è. Usare il prezzo –1 come valore sentinella. Salvare gli input in una
lista, chiamare la funzione implementata, e visualizzare lo sconto.
"""

SCONTO = 20

def discount(prices, is_pet):
    lista_indici = [i for i, el in enumerate(is_pet) if el == False]
    lista_prezzi = [prices[i] for i in lista_indici]
    return sum(lista_prezzi)*20/100




prezzi = []
sono_animali = []

while True:
    prezzo = input("Inserire prezzo: ")
    tipo = input("È un animale (Y/N): ")

    if prezzo == "-1" or tipo == "-1":
        break
    else:
        prezzi.append(float(prezzo))
        if tipo == "Y": tipo=True
        else: tipo=False

        sono_animali.append(tipo)


print(discount(prezzi, sono_animali))