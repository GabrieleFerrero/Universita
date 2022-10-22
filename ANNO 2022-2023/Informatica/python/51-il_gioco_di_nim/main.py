"""
In questo gioco, due giocatori prelevano alternativamente biglie da un
mucchietto. Ad ogni mossa, un giocatore sceglie quante biglie prendere: almeno una e al massimo
metà delle biglie disponibili. Il giocatore che prende l’ultima biglia perde la partita.
Scrivere un programma che consenta all’utente di giocare contro il computer. Il programma deve:
I. generare un numero intero casuale compreso tra 10 e 100 da usare come dimensione
iniziale del mucchietto di biglie;
II. generare un numero intero casuale, o 0 o 1, da usare per decidere se sarà l’utente o il
computer a giocare per primo;
III. generare un numero intero casuale, o 0 o 1, da usare per decidere se il computer giocherà in
modo intelligente o stupido:
a. giocando in modo stupido, ad ogni sua mossa il computer semplicemente preleva
dal mucchietto un numero di biglie casuale (ma valido, cioè compreso tra 1 e n/2,
se nel mucchietto sono rimaste n biglie);
b. giocando in modalità intelligente, invece, preleva un numero di biglie tale che il
numero di quelle che rimangono nel mucchio sia una potenza di due diminuita di
un’unità, cioè 3, 7, 15, 31 o 63. Quest’ultima è sempre una mossa valida, tranne
quando la dimensione del mucchio è uguale a una potenza di due diminuita di
un’unità. In tal caso, il computer fa una mossa scelta a caso (ovviamente tra quelle
valide).
Come potrete verificare sperimentalmente, il computer non può essere battuto quando gioca in
modalità intelligente e fa la prima mossa, a meno che la dimensione iniziale del mucchio non sia 15,
31 o 63. Analogamente, un giocatore umano che faccia la prima mossa e conosca la strategia qui
descritta è in grado di battere il calcolatore.
"""

import random
import math

def mossa_computer():
    global numero_di_biglie

    if numero_di_biglie == 1:
        print("Il computer ha perso!")
        return False

    if tipo_di_gioco_computer == 1:
        numero_biglie_scelte_computer = random.randint(1,int(numero_di_biglie/2))
    else:
        potenza = int(math.log(numero_di_biglie,2))
        numero_biglie_scelte_computer = numero_di_biglie-((2**potenza) - 1)

        if numero_biglie_scelte_computer < 1 or numero_biglie_scelte_computer > int(numero_di_biglie/2):
            numero_biglie_scelte_computer = random.randint(1, int(numero_di_biglie / 2))


    numero_di_biglie -= numero_biglie_scelte_computer
    print(f"Il computer ha scelto di prendere {numero_biglie_scelte_computer} {'biglia' if numero_biglie_scelte_computer == 1 else 'biglie'}")
    print(f"Sono rimaste {numero_di_biglie} {'biglia' if numero_di_biglie == 1 else 'biglie'}")


numero_di_biglie = random.randint(10,100)
primo_turno = random.randint(0,1) # 0 --> computer, 1 --> persona
tipo_di_gioco_computer = random.randint(0,1) # 0 --> intelligente, 1 --> stupido

print(f"Numero biglie: {numero_di_biglie}")
print(f"Inizia {'Computer' if primo_turno==0 else 'Umano'}")
print(f"Il Computer giocherà in modo {'intelligente' if tipo_di_gioco_computer==0 else 'stupido'}")


if primo_turno==0: mossa_computer()

while True:
    if numero_di_biglie == 1:
        print("Hai perso!")
        break

    numero_biglie_scelte_persona = int(input("Inserire il numero delle biglie che vui prendere: "))

    if 1 <= numero_biglie_scelte_persona <= int(numero_di_biglie/2):

        numero_di_biglie -= numero_biglie_scelte_persona
        print(f"Sono rimaste {numero_di_biglie} {'biglia' if numero_di_biglie == 1 else 'biglie'}")

        if mossa_computer()==False: break


