"""
Leggere una sequenza di numeri interi conclusa da una riga vuota. Stampare
la posizione dei massimi locali (numeri maggiori sia del valore precedente che di quello successivo)
se ce ne sono, altrimenti stampare il messaggio 'Non ci sono massimi locali'.
Estensione: se sono presenti più coppie di massimi locali, individuare i due massimi locali più vicini
fra loro e stampare la loro posizione
"""

numeri = []
while True:
    num = input("Inserire numero: ")
    if num == "": break
    else: numeri.append(int(num))


massimi_locali = []
for i, _ in enumerate(numeri):
    if i>0 and i < len(numeri)-1:
        if numeri[i-1] < numeri[i] and numeri[i] > numeri[i+1]: massimi_locali.append([numeri[i],i])


if len(massimi_locali)==0: print("Non ci sono massimi locali")
else: print(massimi_locali)

if len(massimi_locali) >= 2:
    indice = 0
    max1 = [massimi_locali[0][0],0]
    for i, num in enumerate(massimi_locali):
        if num[0] > max1[0]:
            max1[0] = num[0]
            max1[1] = num[1]
            indice = i

    massimi_locali.pop(indice)

    max2 = [massimi_locali[0][0], 0]
    for i, num in enumerate(massimi_locali):
        if num[0] > max2[0]:
            max2[0] = num[0]
            max2[1] = num[1]

    print(max1[1],max2[1])




