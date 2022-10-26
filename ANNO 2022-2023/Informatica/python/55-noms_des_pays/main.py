"""
In francese i nomi delle nazioni sono femminili quando terminano con la
lettera e, altrimenti sono maschili, con l’eccezione dei nomi seguenti, che sono maschili anche se
terminano con la e:
I. le Belize;
II. le Cambodge;
III. le Mexique;
IV. le Mozambique;
V. le Zaïre;
VI. le Zimbabwe.
Scrivere un programma che acquisisca il nome di una nazione in francese e vi aggiunga l’articolo:
'le' per i nomi maschili e 'la' per quelli femminili, come 'le Canada' o 'la Belgique'. Se,
però, il nome della nazione inizia con una vocale, l’articolo diventa 'l’' (ad esempio,
'l’Afghanistan'). Infine, per i paesi qui elencati, che hanno un nome plurale, si usa l’articolo
'les':
VII. les Etats-Unis;
VIII. les Pays-Bas.
"""


nome = input("Inserire il nome della nazione: ").lower()

if nome[-1]=="s":
    print(f"les {nome}")
elif nome[0] in "aeiou":
    print(f"l'{nome}")
elif nome[-1] != "e" or nome=="belize" or nome=="cambodge" or nome=="mexique" or nome=="mozambique" or nome=="zaïre" or nome=="zimbabwe":
    print(f"le {nome}")
else:
    print(f"la {nome}")