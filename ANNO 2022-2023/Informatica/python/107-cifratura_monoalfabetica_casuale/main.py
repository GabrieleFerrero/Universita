"""
Il cifrario di Cesare è un cifrario a sostituzione
monoalfabetica, in cui ogni lettera del testo in chiaro è sostituita, nel testo cifrato, dalla lettera che si
trova un certo numero di posizioni dopo nell'alfabeto. Poiché il numero di posizioni usato per la
traslazione è fisso, il cifrario di Cesare è troppo facile da violare. Per rendere il testo cifrato più
difficile da decifrare, una strategia alternativa è utilizzare come chiave, invece di un numero, una
parola. Ad esempio, se la parola che si usa come chiave è FEATHER, per prima cosa si eliminano le
lettere duplicate, ottenendo FEATHR, e poi si aggiungono in coda le rimanenti lettere dell’alfabeto,
in ordine inverso. Si ottiene così la sequenza seguente.
F E A T H R Z Y X W V U S Q P O N M L K J I G D C B
Poi, si procede alla cifratura delle lettere, secondo lo schema seguente.
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓
F E A T H R Z Y X W V U S Q P O N M L K J I G D C B
Eventuali altri caratteri (ad esempio spazi, cifre, o segni di punteggiatura) devono rimanere invariati.
Scrivere un programma che richieda in input all’utente il nome di un file di testo da cifrare o
decifrare, la scelta di quale operazione compiere (cifratura o decifratura), una parola chiave, e il
nome di un file in cui scrivere l’output dell’elaborazione. Il programma deve memorizzare la parola
chiave inserita dall’utente in una variabile, e utilizzarla per cifrare o decifrare il file di testo fornito in
input, scrivendo poi il risultato delle elaborazioni nel file di output indicato.
"""

import string


def funzione_cifratura_decifratura(nome_file_input, nome_file_output, tabella_conversione, indice_1, indice_2):
    with open(nome_file_input, "r") as file_input:
        with open(nome_file_output, "w") as file_output:
            for riga in file_input:
                for lettera in riga:
                    if lettera.lower() in string.ascii_lowercase:
                        for conversione in tabella_conversione:
                            if conversione[indice_1] == lettera.lower():
                                if lettera in string.ascii_uppercase:
                                    file_output.write(conversione[indice_2].upper())
                                else:
                                    file_output.write(conversione[indice_2])
                    else: file_output.write(lettera)



nome_file_input = input("Nome file input: ").replace(" ", "")
nome_file_output = input("Nome file output: ").replace(" ", "")
scelta = input("Inserire la scelta (cifratura/decifratura): ")
chiave_di_cifratura = input("Inserire la parola di cifratura: ").lower().replace(" ","")



lettere_alfabeto = list(string.ascii_lowercase)
lettere_alfabeto_rovesciato = lettere_alfabeto
lettere_alfabeto_rovesciato.reverse()
nuova_chiave_cifratura = ""
for lettera in list(chiave_di_cifratura)+lettere_alfabeto_rovesciato:
    if lettera not in nuova_chiave_cifratura:
        nuova_chiave_cifratura += lettera
tabella_conversione = [(let_al, let_ci) for let_al, let_ci in zip(lettere_alfabeto, nuova_chiave_cifratura)]
print(tabella_conversione)




if scelta == "cifratura":
    funzione_cifratura_decifratura(nome_file_input, nome_file_output, tabella_conversione, 0, 1)
else:
    funzione_cifratura_decifratura(nome_file_input, nome_file_output, tabella_conversione, 1, 0)



