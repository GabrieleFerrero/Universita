"""
Scrivere un programma che legga il file di testo input.txt, e scriva ogni riga
letta nel file output.txt preceduta dal proprio numero di riga inserito come commento tra
caratteri '/*' e '*/'. Se, ad esempio, il file input.txt contiene il testo:
Enola Gay
è il bombardiere che, il 6 agosto 1945,
sganciò su Hiroshima la prima bomba atomica
soprannominata Little Boy.
il file output.txt generato deve contenere il testo:
/*1*/Enola Gay
/*2*/è il bombardiere che, il 6 agosto 1945,
/*3*/sganciò su Hiroshima la prima bomba atomica
/*4*/soprannominata Little Boy.
"""

with open("./input.txt","r") as file_input:
    with open("./output.txt", "w") as file_output:
        for i, riga in enumerate(file_input.readlines()):
            file_output.write(f"/*{i+1}*/{riga}")