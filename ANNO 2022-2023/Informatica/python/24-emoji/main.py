"""
Secondo i dati raccolti dall'Unicode Consortium1, l'organizzazione no-profit
responsabile della digitalizzazione delle lingue del mondo, le “lacrime di gioia” ( ) rappresentano
oltre il 5% di tutte le emoji utilizzate (l’unico altro carattere che ci si avvicina è il ). Le prime dieci
emoji utilizzate in tutto il mondo sono: .
Quando scambiate messaggi su Telegram (o sulla vostra app di messaggistica preferita), quali sono le
tre emoji che voi personalmente usate più di frequente? Utilizzando le informazioni sulla codifica
Unicode qui raccolte2, scrivere un programma che mostri a schermo, per ciascuna di queste tre
emoji:

I. la posizione in classifica (rank);
II. il Numero Unicode;
III. il Nome Unicode;
IV. l’emoji stessa.

Formattare l’output in modo che le informazioni relative a ciascuna delle tre emoji siano raccolte su
una riga, e i diversi campi siano allineati verticalmente.
"""

top_three = {
    "1F602":{
        "nome":"Affrontare con lacrime di gioia",
        "posizione": 1
    },
    "1F60D":{
            "nome":"Volto con occhi a forma di cuore",
            "posizione": 2
    },
    "1F62D":{
            "nome":"AFaccia ad alta voce",
            "posizione": 3
    }
}

codici_unicode = [codice for codice, _ in top_three.items()]
nomi_unicode = [top_three[codice]["nome"] for codice in top_three]
classifica = [top_three[codice]["posizione"] for codice in top_three]

lunghezza_riga = 107
lunghezza_step = 35
print(f"+{'-'*lunghezza_riga}+")

for caratteristica in [classifica, codici_unicode, nomi_unicode]:
    riga = ""
    for car in caratteristica:
        riga+=f"¦{car}{' '*(lunghezza_step-len(str(car)))}"
    print(riga+"¦")

riga = ""
for cod in codici_unicode:
    riga+=f"¦{chr(int(cod, 16))}{' '*(lunghezza_step-2)}"
print(riga+"¦")

print(f"+{'-' * lunghezza_riga}+")