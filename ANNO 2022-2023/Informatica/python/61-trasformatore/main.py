"""
I trasformatori sono spesso costruiti avvolgendo bobine di filo attorno a un
nucleo di ferrite. La figura illustra una situazione che si verifica in vari dispositivi audio come i
telefoni cellulari e i lettori musicali e lettori musicali. In questo circuito, un trasformatore viene
utilizzato per collegare un altoparlante all'uscita di un amplificatore audio all'uscita di un
amplificatore audio.
Il simbolo utilizzato per rappresentare il trasformatore intende suggerire due bobine di filo. Il
parametro 𝑛 del trasformatore è chiamato "rapporto di spire" del trasformatore. (Il numero di volte
in cui un filo viene avvolto intorno al nucleo per formare una bobina è chiamato è chiamato "numero
di spire" della bobina. Il rapporto di spire è letteralmente il rapporto tra il numero di spire nelle due
bobine di filo). Quando si progetta il circuito, ci si preoccupa soprattutto del valore della potenza
14BHD Informatica, A.A. 2022/23 Lab05
4
erogata ai diffusori: tale potenza fa sì che i diffusori producano i suoni che vogliamo sentire.
Supponiamo di collegare i diffusori direttamente all'amplificatore senza utilizzare il trasformatore.
Una parte della potenza disponibile dall'amplificatore arriverebbe ai diffusori. Il resto della potenza
disponibile andrebbe persa nell'amplificatore stesso. Il trasformatore viene aggiunto al circuito per
aumentare la frazione di potenza dell'amplificatore che arriva ai diffusori. La potenza 𝑃𝑠 erogata ai
diffusori si calcola con la formula
𝑃𝑠 = 𝑅𝑠 ( 𝑛𝑉𝑠
𝑛2𝑅0 + 𝑅𝑠
)
2
Scrivere un programma che modelli il circuito mostrato e vari il rapporto di spire da 0.01 a 2 con
incrementi di 0.01, quindi determinare il valore del rapporto di spire che massimizza la potenza
erogata agli altoparlanti.
"""

R0 = 220
Rs = 8
Vs = 40

min_n = 0.01
max_n = 2

incremento = 0.01

max_potenza = -1

for n in range(int(min_n*100),int(max_n*100)):
    potenza = Rs*(((n*Vs)/((n**2)*R0)+Rs)**2)

    if potenza > max_potenza: max_potenza = potenza

print(f"Max potenza: {max_potenza}")