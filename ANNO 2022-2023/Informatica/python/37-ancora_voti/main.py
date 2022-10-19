"""
Considerando i valori numerici dei voti spiegati nell’esercizio 03.2.2, scrivere un
programma che traduca un numero compreso tra 0.0 e 4.0 nel voto letterale ad esso più vicino. Ad
esempio, il numero 2.8 (che potrebbe essere la media di più voti) deve essere tradotto come 'B–'.
Risolvete i casi di parità in favore del voto migliore: ad esempio, 2.85 deve essere tradotto come
'B'.
"""


def arrotondamento(numero):
    parte_decimale = numero%(int(numero))
    if parte_decimale >= 0.85 or parte_decimale <= 0.15: return f"{corrispondenza[int(valore)]}"
    elif parte_decimale >= 0.50 and parte_decimale < 0.85: return f"{corrispondenza[int(valore)+1]}-"
    elif parte_decimale > 0.15 and parte_decimale < 0.55: return f"{corrispondenza[int(valore)]}+"


corrispondenza = {4:"A",3:"B",2:"C",1:"D",0:"F"}


valore = float(input("Inserire il numero: "))
if valore > 4: valore = 4
if valore < 0: valore = 0

print(f"Il numero convertito è: {arrotondamento(valore)}")

