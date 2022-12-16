"""
Un vettore sparso è una sequenza di numeri, la maggior parte dei quali è 0.
Un modo efficiente per memorizzare un vettore sparso è un dizionario, nel quale le chiavi sono le
posizioni in cui sono presenti i soli valori diversi da zero, e i valori sono i corrispondenti valori nella
sequenza. Per esempio, la sequenza 0 0 0 0 0 4 0 0 0 2 9 sarebbe rappresentata dal
dizionario {5:4, 9:2, 10:9}. Scrivere una funzione, sparse_array_sum(a, b), i cui
argomenti sono due dizionari di questo tipo, a e b. La funzione, senza modificare i dizionari passati
come argomenti, deve restituire il loro vettore somma come un vettore sparso, dove un valore nella
posizione i è la somma dei valori di a e b nelle rispettive posizioni i.
"""

def sparse_array_sum(a, b):
    new_dict = {}
    for pos in set(a).union(set(b)):
        valore1 = 0
        if pos in a: valore1 = a[pos]
        valore2 = 0
        if pos in b: valore2 = b[pos]
        new_dict[pos] = valore1+valore2

    vettore_sparso = []
    pos_prec = -1
    for pos in new_dict:
        tappo = [0]*(pos-pos_prec-1)
        pos_prec = pos
        vettore_sparso += tappo
        vettore_sparso.append(new_dict[pos])

    return vettore_sparso


a = {5:4, 9:2, 10:9}
b = {5:6, 9:4, 1:9}

print(sparse_array_sum(a,b))