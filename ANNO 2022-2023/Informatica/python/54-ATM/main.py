"""
Quando utilizzate uno sportello bancario automatico (ATM, Automatic Teller Machine)
con la vostra carta, dovete usare un numero identificativo personale (PIN, Personal Identification
Number) per poter accedere al vostro conto. Se un utente sbaglia tre volte l’inserimento del PIN, la
macchina trattiene la carta e la blocca. Nell’ipotesi che il PIN dell’utente sia 1234, scrivere un
programma che chieda all’utente di digitare il PIN, consentendo al massimo tre tentativi e funzioni in
questo modo:
I. quando l’utente inserisce il numero corretto, visualizza il messaggio 'Your PIN is
correct' e termina;
II. quando l’utente inserisce un numero sbagliato, visualizza il messaggio 'Your PIN is
incorrect' e, se avete chiesto il PIN meno di tre volte, lo chiede di nuovo;
III. quando l’utente inserisce un numero sbagliato per tre volte, visualizza il messaggio 'Your
bank card is blocked' e termina.
"""

pin = "1234"

errore = True
for _ in range(3):
    pin_inserito = input("Inserisci pin: ")
    if pin_inserito == pin:
        print("Your PIN is correct")
        errore = False
        break
    else: print("Your PIN is incorrect")

if errore: print("Your bank card is blocked")


