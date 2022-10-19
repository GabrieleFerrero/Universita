"""
Le sequenze di DNA sono come lunghe stringhe composte da solo
quattro lettere: 'A', 'C', 'T' e 'G'. Scrivere un programma che prende in input una “sequenza
lunga” di DNA di venti caratteri e una “sequenza breve” di tre caratteri e visualizza:
I. se la “sequenza lunga” contiene la “sequenza breve”;
II. se presente, a partire da quale posizione della “sequenza lunga” è presente la “sequenza
breve”;
III. se presente, quante volte la sequenza “lunga” contiene la sottostringa più breve.
"""

seq_lunga = input("Sequenza lunga: ")
seq_breve = input("Sequenza breve: ")

if seq_breve in seq_lunga: print("“sequenza lunga” contiene la “sequenza breve”")
pos_inizio_seq_breve = []
copia_seq_lunga = seq_lunga
while copia_seq_lunga.find(seq_breve)!=-1:
    pos_inizio_seq_breve.append(copia_seq_lunga.find(seq_breve)+(len(pos_inizio_seq_breve)*len(seq_breve))) # io sommo all'inidice trovato la lunghezza delle sequenze brevi rimosse in precedenza
    copia_seq_lunga = copia_seq_lunga.replace(seq_breve, "", 1)

print(pos_inizio_seq_breve)

print(len(pos_inizio_seq_breve))