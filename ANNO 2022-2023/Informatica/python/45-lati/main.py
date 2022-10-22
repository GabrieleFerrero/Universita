"""
Scrivere un programma che legga un numero intero n e visualizzi, usando asterischi (*),
un quadrato e un rombo pieni, il cui lato abbia lunghezza n. Se, ad esempio, l’utente fornisce il
numero 4, il programma deve visualizzare:
****
****
****
****
*
***
*****
*******
*****
***
*
"""

lunghezza_lato = int(input("Insereire lunghezza lato: "))

for _ in range(lunghezza_lato):
    for _ in range(lunghezza_lato):
        print("*", end="")
    print("\n",end="")

print("\n")

for i in range(lunghezza_lato):
    print(f"{' '*(int((((lunghezza_lato*2)-1)/2))-i)}{'*'*i}*{'*'*i}{' '*(int((((lunghezza_lato*2)-1)/2))-i)}", end="")
    print("\n", end="")

for i in range(lunghezza_lato-2, -1, -1): # vado fino a -1 così includo lo zero
    print(f"{' '*(int((((lunghezza_lato*2)-1)/2))-i)}{'*'*i}*{'*'*i}{' '*(int((((lunghezza_lato*2)-1)/2))-i)}", end="")
    print("\n", end="")