"""
Scrivere un programma che legga tre numeri e visualizzi il messaggio “increasing”
se sono in ordine strettamente crescente, “decreasing” se sono in ordine strettamente decrescente
e “neither” se non sono né in ordine crescente né in ordine decrescente. “Strettamente crescente”
significa che ciascun valore deve essere maggiore del precedente (analogo significato ha il termine
decrescente): la sequenza 3 4 4, quindi, non va considerata crescente.
"""


def crescente(lista, numero_precedente):
    if len(lista) > 0:
        nuovo_numero = lista.pop(0)
        if nuovo_numero > numero_precedente:
            return crescente(lista, nuovo_numero)
        else: return False
    else:return True

def decrescente(lista, numero_precedente):
    if len(lista) > 0:
        nuovo_numero = lista.pop(0)
        if nuovo_numero < numero_precedente:
            return decrescente(lista, nuovo_numero)
        else: return False
    else: return True

numeri = []
for i in range(3):
    numeri.append(int(input(f"Inserire numero {i}: ")))


if crescente(numeri[:], min(numeri)-1): print("La sequenza è strettamente crescente")
elif decrescente(numeri[:], max(numeri)+1): print("La sequenza è strettamente decrescente")
else: print("La sequenza è neither")