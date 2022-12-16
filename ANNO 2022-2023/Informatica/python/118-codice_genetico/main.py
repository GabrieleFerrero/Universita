"""
Nelle cellule viventi, l’acido desossiribonucleico (DNA) contiene le
informazioni fondamentali perché l’organismo svolga tutte le funzioni utili alla vita. Per supportare le
funzioni della cellula, le istruzioni contenute nel DNA vengono prima trascritte in molecole di acido
ribonucleico (RNA). Poi, queste molecole di RNA vengono tradotte in proteine. La traduzione da RNA
messaggero (mRNA) a proteine si basa sul codice genetico, cioè l'insieme delle regole con le quali
una sequenza di nucleotidi ('A', 'C', 'U' e 'G') viene tradotta in una sequenza di amminoacidi
per la sintesi proteica. Ciascun amminoacido corrisponde a una o più sequenze di tre nucleotidi, che
vengono chiamate codoni. La tabella seguente1 riporta i codoni che in un mRNA codificano i 20
amminoacidi ordinari.
1 Codice genetico (Wikipedia): https://it.wikipedia.org/wiki/Codice_genetico

Amminoacido Codoni Amminoacido Codoni
Ala GCU, GCC, GCA, GCG Leu UUA, UUG, CUU, CUC, CUA,
CUG
Arg CGU, CGC, CGA, CGG, AGA,
AGG
Lys AAA, AAG
Asn AAU, AAC Met AUG
Asp GAU, GAC Phe UUU, UUC
Cys UGU, UGC Pro CCU, CCC, CCA, CCG
Gln CAA, CAG Ser UCU, UCC, UCA, UCG, AGU,
AGC
Glu GAA, GAG Thr ACU, ACC, ACA, ACG
Gly GGU, GGC, GGA, GGG Trp UGG
His CAU, CAC Tyr UAU, UAC
Ile AUU, AUC, AUA Val GUU, GUC, GUA, GUG
I seguenti codoni indicano le istruzioni di inizio e di fine del processo di traduzione. Si noti che il
codone di start codifica anche la Metionina ('Met').
Istruzione Codoni
start AUG, GUG
stop UAG, UGA, UAA
Scrivere un programma che elabori una sequenza di mRNA inserita in input dall’utente, e visualizzi la
sequenza di amminoacidi da essa tradotta. Per simulare il processo di traduzione, utilizzare un
dizionario genetic_code, che, leggendo le informazioni riportate in tabella dal file
codice_genetico.csv, memorizzi i codoni e gli amminoacidi da essi codificati, scegliendo in
modo opportuno quale categoria utilizzare come chiavi e quale come valori. Poi, scorrere la
sequenza inserita dall’utente fino a che non si trova una corrispondenza con uno dei codoni di
'start'. Scorrere infine la parte successiva della sequenza, memorizzando il risultato della
traduzione di ciascun codone in una lista protein. La traduzione si deve interrompere quando si
incontra un codone di 'stop'. Ad esempio, partendo dalla sequenza di nucleotidi (i codoni di
'start' e di 'stop' sono sottolineati), GUAUGCACGUGACUUUCCUCAUGAGCUGAU il programma
deve visualizzare: MetHisValThrPheLeuMetSerstop. La prima occorrenza dell’amminoacido
'Met' (Metionina), il cui codone corrisponde alla sequenza di 'start' e il punto di 'stop' sono
sottolineati. Se lo scorrimento arriva alla fine della sequenza senza incontrare entrambi i codoni di
'start' e di 'stop', allora il programma deve restituire un messaggio di errore.
"""


import csv

protein = ""

contenuto = {}

with open("codice_genetico.csv", "r", encoding="utf-8") as file_csv:
    file = csv.reader(file_csv, delimiter=",")
    for riga in file:
        riga[0] = riga[0].replace("\xa0","")
        riga[1] = riga[1].replace("\xa0","")

        contenuto[riga[0]] = riga[1].replace(" ","").split(",")

print(contenuto)

lettere = ""
inizio = False
esci = False
while not esci:
    lettere += input("Inserire lettera: ").upper()

    #print(lettere)

    new_lettere = lettere
    i=0
    while i < len(lettere):
        aumentato = False
        # estraggo sequenza
        sequenza = ""
        for y in range(i, i+3):
            if y < len(lettere):
                sequenza += lettere[y]
        # cerco valore corrispondente
        if len(sequenza) == 3:
            trovato = False
            for key,value in contenuto.items():
                if sequenza in value:
                    trovato=True
                    if key=="stop":
                        esci=True
                    elif key=="start" or key=="Met":
                        key="Met"
                        inizio=True
                    if inizio:
                        #print(key)
                        protein += key
                        break
            if inizio:
                if trovato:
                    new_lettere = new_lettere[3:]
                    aumentato = True
                    i+=3
                else:
                    new_lettere = new_lettere[1:]
                    aumentato = True
                    i+=1
            else:
                new_lettere = new_lettere[1:]
                aumentato = True
                i += 1
        if not aumentato:
            i+=1

    lettere = new_lettere


print(protein)