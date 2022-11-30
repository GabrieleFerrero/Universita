"""
Nei lunghi viaggi in treno, per ingannare il tempo, si può fare il gioco
delle “parole concatenate”. Il primo giocatore dice una parola iniziale, poi a turno ciascun giocatore
dovrà dire una parola non ancora detta durante la partita, la cui sillaba iniziale sia uguale alla sillaba
finale della parola precedente. Un esempio di sequenza è: 'gatto', 'torino', 'notte',
'tela', 'lana'. Per semplicità, ipotizziamo che tutte le sillabe siano lunghe esattamente 2
caratteri. Quindi, ad esempio, per 'figli' la sillaba finale sarà 'li' e non 'gli'.
Scrivere un programma per permettere di gestire una o più partite del gioco. Ciascuna partita
termina quando uno dei giocatori inserisce una parola già detta durante stessa partita, quando
inserisce una parola concatenata in modo scorretto, oppure quando non riesce a inserire una nuova
parola. Per abbandonare la partita, il giocatore di turno deve inserire un asterisco (*)
"""

parole_dette = []

parola = input("Inserire la prima parola: ")
if parola != "*":
    parole_dette.append(parola)
    ultima_sillaba = parola[-2:]
    print(f"Ultima sillaba: {ultima_sillaba}")

    while True:
        parola = input("Inserire la parola: ")
        if parola == "*": break

        if parola != "" and parola not in parole_dette and parola[0:2] == ultima_sillaba:
            parole_dette.append(parola)
            ultima_sillaba = parola[-2:]
        else:
            print("Hai perso")
            break

        print(f"Ultima sillaba: {ultima_sillaba}")