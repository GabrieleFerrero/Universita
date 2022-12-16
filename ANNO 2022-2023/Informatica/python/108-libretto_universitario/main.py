"""
Scrivere un programma che visualizzi l’elenco degli esami superati da
uno studente, con i relativi voti. È disponibile un file classes.txt, che contiene i codici di tutti i
corsi erogati nell’istituto scolastico (un college statunitense), il cui contenuto sarà simile a questo:
CSC1
CSC2
CSC46
CSC151
MTH121
...
Per ciascun corso, è disponibile un file il cui nome corrisponde al codice del corso, seguito da
'.txt'. Questo file elenca le persone che hanno superato l’esame del corso, riportando per
ciascuna il numero identificativo ('Student ID') e il voto ottenuto. Ad esempio, il file CSC2.txt
potrebbe contenere il testo:
11234 A–
12547 B
16753 B+
21886 C
...
Scrivere un programma che richieda all’utente di inserire in input uno 'Student ID', e visualizzi
poi l’elenco degli esami superati ad esso associati, riportando i voti ottenuti per ciascun esame,
rispettando il seguente formato.
Student ID: 16753
CSC2 B+
MTH121 C+
CHN1 A
PHY50 A–
"""

classi = []
with open("classes.txt", "r") as file_classi:
    for classe in file_classi:
        classi.append(classe.upper().replace("\n", ""))

id_studente = input("Studente id: ").replace(" ", "").upper()
print(f"Student ID: {id_studente}")

for classe in classi:
    with open(f"{classe}.txt", "r") as file:
        for riga in file:
            if id_studente in riga:
                riga = riga.replace("\n","")
                print(f"{classe} {riga.split(' ')[1]}")