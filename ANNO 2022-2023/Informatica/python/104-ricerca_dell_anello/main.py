"""
Scrivere un programma che cerchi una data parola nel contenuto di un
gruppo di file. Il programma deve chiedere all’utente di inserire in input:
I. un elenco di nomi di file su una sola riga, separati da virgole;
II. una parola da cercare.
I nomi dei file devono essere memorizzati in una lista, mentre la parola da cercare deve essere
memorizzata in una variabile. Il programma deve visualizzare tutte le righe che contengono la
parola, anche come sottostringa di altre parole, senza distinzione tra lettere maiuscole e minuscole.
Ciascuna riga visualizzata deve essere preceduta dal nome del file in cui si trova. Ad esempio, se la
parola da cercare è 'ring', e la lista contiene i file:
book.txt, address.txt, homework.py
allora il programma, elaborato il contenuto di tali file, deve visualizzare le righe dove si trova la
parola da cercare con il seguente formato:
book.txt: There is only one Lord of the Ring, only one who can bend it to
his will
book.txt: The ring has awoken; it’s heard its master’s call.
address.txt: Kris Kringle, North Pole
address.txt: Homer Simpson, Springfield
homework.py: string = "text"
"""


nomi_file = input("Inserire il nome dei file: ")
nomi_file = nomi_file.replace(" ","").split(",")

parola_da_cercare = input("Inserire la parola da cercare: ")
parola_da_cercare = parola_da_cercare.lower()

contenuto_file = {}
for nome_file in nomi_file:
    file = open(nome_file, "r")
    contenuto_file[nome_file] = file.readlines()
    file.close()

for file, contenuto in contenuto_file.items():
    for riga in contenuto:
        if parola_da_cercare in riga.lower():
            riga = riga.replace('\n','')
            print(f"{file}: {riga}")