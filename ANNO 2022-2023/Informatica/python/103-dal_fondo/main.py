"""
Scrivere un programma che legga tutte le righe di un file di testo input.txt, ne
inverta l’ordine e le scriva in un altro file output.txt. Ad esempio, se il file input.txt contiene il
testo:
Mary had a little lamb
Its fleece was white as snow
And everywhere that Mary went
The lamb was sure to go.
il file output.txt generato deve contenere il testo:
The lamb was sure to go.
And everywhere that Mary went
Its fleece was white as snow
Mary had a little lamb
"""


file_input = open("input.txt", "r")
file_output = open("output.txt", "w")
contenuto = file_input.readlines()
contenuto.reverse()
for riga in contenuto:
    file_output.write(riga)

file_input.close()
file_output.close()
