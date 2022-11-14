"""
Il gioco del Solitario bulgaro inizia con 45 carte. Le carte vengono divise a
caso in un dato numero di pile con dimensioni casuali. Ad esempio, si può iniziare con 5 pile di
dimensioni 20, 5, 1, 9 e 10. Ad ogni turno, si sottrae una carta da ciascuna pila, e si crea una
nuova pila composta dalle carte sottratte dalle pile di partenza. Ad esempio, la configurazione di
partenza verrebbe trasformata in pile di dimensioni 19, 4, 8, 9 e 5. Il gioco finisce quando le pile
hanno dimensioni 1, 2, 3, 4, 5, 6, 7, 8 e 9 (si può dimostrare che si ottiene sempre una
configurazione di questo tipo). Scrivere un programma che generi una configurazione iniziale casuale
e la visualizzi, e che poi continui con i passi del solitario, visualizzando la configurazione dopo ciascun
passo, e fermandosi quando si raggiunge la configurazione finale del solitario.
"""


import random

num_carte = 45

num_pile = int(input("Inserire il numero di pile: "))

pile = [random.randint(1,num_carte-num_pile+1)]
for i in range(1, num_pile-1):
    pile.append(random.randint(1, num_carte-sum(pile)-num_pile+i))
pile.append(num_carte-sum(pile))

print(pile)


while pile != [0,1,2,3,4,5,6,7,8,9]:
    new_pile = []

    for i in range(len(pile)):
        if pile[i] != 0:
            new_pile.append(pile[i]-1)

    new_pile.append(len(new_pile))
    pile = new_pile[::]
    print(pile)
    print(f"La somma è {sum(pile)}")



