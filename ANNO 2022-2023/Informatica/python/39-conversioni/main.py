"""
Scrivere un programma per la conversione di unità di misura che chieda
all’utente: l’unità di misura di partenza (scegliendo tra: ml, l, g, kg, mm, cm, m, km); l’unità di misura
verso la quale vuole effettuare una conversione (scegliendo tra: fl, oz, gal, lb, in, ft, mi),
rifiutando conversioni incompatibili (come, ad esempio, da km a gal); il valore da convertire. Il
programma deve visualizzare i dati inseriti e il valore derivante dalla conversione.
"""

unita_di_partenza = input("Inserire unità di misura di partenza: ")
unita_di_arrivo = input("Inserire unità di misura di arrivo: ")
valore = input("Inserire il valore da convertire: ")

conversioni = {
    "l": {
        "fl":"*1000000000",
        "gal":"*0.264172",
    },
    "ml": {
        "fl":"*1000000000/1000",
        "gal":"*0.264172/1000",
    },
    "g":{
        "oz":"*0.035274",
        "lb":"*0.00220462"
    },
    "kg":{
        "oz":"*0.035274*1000",
        "lb":"*0.00220462*1000"
    },
    "mm":{
        "in":"*39.3701/1000",
        "ft":"*3.28084/1000",
        "mi":"*0.000621371/1000"
    },
    "cm":{
        "in":"*39.3701/100",
        "ft":"*3.28084/100",
        "mi":"*0.000621371/100"
    },
    "m":{
        "in":"*39.3701",
        "ft":"*3.28084",
        "mi":"*0.000621371"
    },
    "km":{
        "in":"*39.3701*1000",
        "ft":"*3.28084*1000",
        "mi":"*0.000621371*1000"
        }
}


if not(unita_di_partenza in conversioni and unita_di_arrivo in conversioni[unita_di_partenza]): exit("Dati inseriti errati")

print(f"{unita_di_partenza} --> {unita_di_arrivo}\nvalore: {valore}\nrisultato: {eval(str(valore)+conversioni[unita_di_partenza][unita_di_arrivo])}")
