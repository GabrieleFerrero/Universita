"""
È possibile decifrare un testo mediante la semplice analisi della frequenza di
occorrenza di singole lettere. Un modo per ostacolare questa strategia consiste nel cifrare in modo
congiunto coppie di lettere. Il cifrario Playfair è un semplice schema che applica questa strategia. In
questo schema, come prima cosa si sceglie una parola chiave, e si eliminano le lettere in essa
duplicate. Poi si inserisce la parola chiave così elaborata in una scacchiera 5 × 5, seguita dalle
rimanenti lettere dell’alfabeto inglese in ordine. Dato che ci sono soltanto 25 caselle e l’alfabeto
inglese ha 26 lettere, la 'I' e la 'J' sono considerate indistinguibili. Verificare che nel testo sorgente le
lettere siano pari, sennò aggiungere una 'Z'. Usando 'PLAYFAIR', trasformata in 'PLAYFIR', come
parola chiave, si ottiene il seguente schema.
P L A Y F
I R B C D
E G H K M
N O Q S T
U V W X Z
Partendo da questa tabella, per cifrare una coppia di lettere, ad esempio 'AM', si individua la
porzione di tabella che presenta 'A' ed 'M' a due estremi:
P L A Y F
I R B C D
E G H K M
N O Q S T
U V W X Z
La codifica della coppia 'AM' si ottiene trovando i valori ai due estremi restanti della porzione di
tabella, in questo caso, 'FH'. Se le due lettere della coppia si trovano sulla stessa riga oppure sulla
stessa colonna, come ad esempio, la coppia 'GO', la codifica si esegue scambiando le lettere tra
loro, ottenendo, in questo caso, 'OG'. La decifrazione segue le stesse regole. Scrivere un
programma che cifri o decifri un file di testo secondo lo schema del cifrario Playfair.
"""

import string
from time import sleep


def trova_lettera(matrice, lettera):
    for y in range(len(matrice)):
        for x in range(len(matrice[y])):
            if matrice[y][x] == lettera:
                return (y,x)


def funzione_cifratura_decifratura(nome_file_input, nome_file_output, tabella_conversione):
    with open(nome_file_input, "r") as file_input:
        with open(nome_file_output, "w") as file_output:
            for riga in file_input:
                riga = riga.replace("\n","")
                for parola in riga.split():
                    parola = parola.replace("j","i")

                    i=0
                    while i < len(parola):
                        lettera_1 = parola[i]
                        if lettera_1.lower() not in string.ascii_lowercase:
                            file_output.write(lettera_1)
                            i+=1
                        else:
                            if i == len(parola)-1:
                                lettera_2 = "z"
                            else:
                                lettera_2 = parola[i+1]
                                if lettera_2.lower() not in string.ascii_lowercase:
                                    lettera_2 = "z"

                            y_1,x_1 = trova_lettera(tabella_conversione, lettera_1.lower())
                            y_2,x_2 = trova_lettera(tabella_conversione, lettera_2.lower())

                            if y_1 == y_2 or x_1 == x_2: lettera_1,lettera_2 = lettera_2,lettera_1
                            else:
                                lettera_1_temp = tabella_conversione[y_1][x_2]
                                lettera_2_temp = tabella_conversione[y_2][x_1]

                                if lettera_1.isupper(): lettera_1 = lettera_1_temp.upper()
                                else: lettera_1 = lettera_1_temp
                                if lettera_2.isupper(): lettera_2 = lettera_2_temp.upper()
                                else: lettera_2 = lettera_2_temp

                            file_output.write(f"{lettera_1}{lettera_2}")

                            if i < len(parola)-1:
                                lettera_2 = parola[i+1]
                                if lettera_2.lower() not in string.ascii_lowercase:
                                    file_output.write(lettera_2)
                            i+=2
                    file_output.write(" ")
                file_output.write("\n")


chiave_di_cifratura = input("Inserire la parola di cifratura: ").lower().replace(" ","").replace("j","i")

lettere_alfabeto = list(string.ascii_lowercase.replace("j",""))
nuova_chiave_cifratura = ""
for lettera in list(chiave_di_cifratura)+lettere_alfabeto:
    if lettera not in nuova_chiave_cifratura:
        nuova_chiave_cifratura += lettera

tabella_cifratura = []
riga = []
for i, lettera in enumerate(nuova_chiave_cifratura):
    riga.append(lettera)
    if (i+1)%5 == 0:
        tabella_cifratura.append(riga)
        riga=[]

tabella_decifratura = []
for y in range(5):
    riga = []
    for x in range(4,-1,-1):
        riga.append(tabella_cifratura[y][x])
    tabella_decifratura.append(riga)

print("Tabella di cifratura: ")
for riga in tabella_cifratura:
    print(riga)
print("Tabella di decifratura: ")
for riga in tabella_decifratura:
    print(riga)

funzione_cifratura_decifratura("input.txt","output.txt",tabella_cifratura)
funzione_cifratura_decifratura("output.txt","output1.txt",tabella_decifratura)