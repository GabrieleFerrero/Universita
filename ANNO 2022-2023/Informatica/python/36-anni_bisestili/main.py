"""
Un anno di 366 giorni viene detto bisestile e serve a mantenere il calendario
sincronizzato con il Sole, dal momento che la Terra vi ruota attorno una volta ogni 365.25 giorni
circa. In realtà, questo numero non è esatto, e per tutte le date successive al 1582 si applica la
correzione gregoriana: solitamente gli anni divisibili per 4, come il 1996, sono bisestili, ma gli anni
divisibili per 100, come il 1900, non lo sono; come eccezione all’eccezione, gli anni divisibili per 400,
come il 2000, sono bisestili. Scrivere un programma che chieda all’utente un anno (maggiore del
1582) e determini se si tratta di un anno bisestile usando un unico costrutto if e gli operatori
booleani.
"""


anno = int(input("Inserire anno: "))

if anno > 1582 and ((anno%4==0 and anno%100!=0) or (anno%400==0)): print(f"L'anno {anno} è bisestile")
else: print(f"L'anno {anno} non è bisestile")