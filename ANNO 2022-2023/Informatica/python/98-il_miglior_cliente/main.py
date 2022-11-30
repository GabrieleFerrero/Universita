"""
Un supermercato vuole ricompensare il proprio miglior cliente del giorno,
mostrandone il nome su uno schermo all’interno del negozio. A questo scopo, vengono memorizzati
in una lista (customers) i nomi di tutti i clienti del giorno e, in un’altra lista (sales), l’importo della
spesa effettuata da ciascuno di loro. Scrivere la funzione name_of_best_customer(sales,
customers) che restituisca il nome del cliente che ha speso la cifra più alta. Poi, scrivere un
programma che chieda al cassiere di digitare tutti gli importi spesi e i nomi dei relativi clienti,
aggiungendoli, dopo ciascuna acquisizione, a due liste distinte, per poi invocare la funzione
progettata e visualizzare il risultato. Usate il l'importo 0 come sentinella.
"""

customers = []
sales = []


def name_of_best_customer(sales, customers):
    spesa_massima = max(sales)
    return customers[sales.index(spesa_massima)], spesa_massima




while True:
    cliente = input("Inserire nome cliente: ")
    spesa = input("Inserire spesa del cliente: ")

    spesa = float(spesa)

    if spesa == 0: break

    if cliente in customers:
        indice = customers.index(cliente)
        sales[indice] += spesa
    else:
        customers.append(cliente)
        sales.append(spesa)



print(name_of_best_customer(sales, customers))

