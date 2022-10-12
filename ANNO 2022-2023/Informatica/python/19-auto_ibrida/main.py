"""
Scrivere lo pseudocodice e il relativo programma Python che aiuta una persona a
decidere se comprare o meno un’auto ibrida. Gli input del programma dovrebbero essere:
    I. il costo di un’auto nuova;
    II. la stima dei chilometri percorsi in un anno;
    III. La stima del costo del carburante;
    IV. L’efficienza in chilometri al litro;
    V. La stima del valore di rivendita dell’auto usata dopo 5 anni.

Calcolare il costo totale di proprietà dell’auto per 5 anni (per semplicità, non tenere in
considerazione il costo di finanziamenti). Per fornire gli input al programma, ricercare sul Web prezzi
e consumi realistici per due alternative per l’acquisto di un’auto nuova nella stessa fascia di prezzo:
un modello ibrido e uno a benzina.

Eseguire il programma due volte per comparare le due
alternative, considerando l’attuale prezzo del carburante e la previsione di percorrere 30’000
chilometri all’anno.
"""


costo_auto_nuova = float(input("Inserire prezzo auto nuova: "))
stima_km_percorsi_in_un_anno = float(input("Inserire la stima dei km percorsi in un anno: "))
stima_costo_carburante_al_litro = float(input("Inserire la stima del costo del carburante: "))
efficienza_km_al_litro = float(input("Inserire l'efficienza km al litro: "))
stima_valore_di_rivendita = float(input("Inserire la stima del valore di rivendita: "))
numero_di_anni_tenuta_auto = float(input("Inserire il numero di anni per i quali si vuole tenere l'auto: "))


carburante_usato_in_un_anno = stima_km_percorsi_in_un_anno*(efficienza_km_al_litro**-1)
costo_carburante_in_un_anno = carburante_usato_in_un_anno*stima_costo_carburante_al_litro
costo_carburante_totale_anni = costo_carburante_in_un_anno*numero_di_anni_tenuta_auto

sconvenienza = (costo_carburante_totale_anni + costo_auto_nuova) - stima_valore_di_rivendita

print(f"La sconvenienza di questa auto è: {sconvenienza}")