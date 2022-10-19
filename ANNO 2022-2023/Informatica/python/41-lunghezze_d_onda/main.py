"""
Scrivere un programma che chiede in input all’utente un valore di
lunghezza d’onda (numero reale, che potrà essere scritto in notazione scientifica, ad esempio
1.23e-7), e visualizza la descrizione della parte corrispondente dello spettro elettromagnetico,
come illustrato nella tabella seguente
"""

lunghezza_onda = float(input("Inserire la lunghezza d'onda: "))

if lunghezza_onda > 10e-1: print(f"Tipo onda: {'Onde Radio':<20}| Frequenza: < 3×10e9")
elif 10e-3 < lunghezza_onda <= 10e-1: print(f"Tipo onda: {'Microonde':<20}| Frequenza: Da 3×10e9 a 3×10e11")
elif 10e-7 < lunghezza_onda <= 10e-3: print(f"Tipo onda: {'Infrarossi':<20}| Frequenza: Da 3×10e11 a 4×10e14")
elif 10e-7 < lunghezza_onda <= 10e-7: print(f"Tipo onda: {'Luce visibile':<20}| Frequenza: Da 4×10e14 a 7.5×10e14")
elif 10e-8 < lunghezza_onda <= 10e-7: print(f"Tipo onda: {'Ultravioletti ':<20}| Frequenza: Da 7.5×10e14 a 3×10e16")
elif 10e-11 < lunghezza_onda <= 10e-8: print(f"Tipo onda: {'Raggi X':<20}| Frequenza: Da 3×10e16 a 3×10e19")
elif lunghezza_onda <= 10e-11: print(f"Tipo onda: {'Raggi Gamma':<20}| Frequenza: > 3×10e19")

