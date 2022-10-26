"""
Le equazioni di Lotka-Volterra descrivono un modello ecologico predatore-
preda che si basa su un insieme di costanti positive fisse:
A. il tasso di crescita delle prede;
B. il tasso di distruzione delle prede da parte dei predatori;
C. il tasso di mortalità dei predatori);
D. il tasso di incremento dei predatori attraverso il consumo delle prede.
Considerate queste costanti, in questo modello valgono le seguenti condizioni:
I. una popolazione di prede x aumenta a un tasso dx=Ax dt (proporzionale al numero di
prede) ma viene contemporaneamente distrutta dai predatori a un tasso
dx=− B xy dt (proporzionale al prodotto dei numeri di prede e predatori);
II. una popolazione di predatori y diminuisce a un tasso dy = − C y dt
dy = − C y dt
(proporzionale al numero di predatori), ma aumenta a un tasso dy = D xy dt (proporzionale
al prodotto del numero di prede e predatori).
Da queste condizioni, deriva il sistema di equazioni differenziali:
dx/dt =Ax − Bxy
dy/dt =−Cy + Dxy
Questo significa che, considerati due periodi di tempo n
e n + 1, la variazione della numerosità delle
popolazioni di, rispettivamente, prede (x) e predatori (y), da un periodo al successivo è data da:
xn+1 = xn×(1+A−B×yn)
yn+1 = y×(1−C+D×xn)
Scrivere un programma che richiede in input all’utente il valore delle quattro costanti, le numerosità
iniziali delle popolazioni di prede e predatori, e il numero di periodi che si desidera simulare, per poi
calcolare e visualizzare la numerosità delle due popolazioni in ciascuno dei periodi considerati. Come
input di prova, usare A = 0.1, B = 0.01, C = 0.01 e D = 0.00002, con popolazioni iniziali di
prede e predatori con numerosità pari a 1000 e 20, rispettivamente.
"""

tasso_di_crescita_delle_prede = float(input("Inserire il tasso di crescita delle prede: "))
tasso_di_distruzione_delle_prede_da_parte_dei_predatori = float(input("Inserire il tasso di distruzione delle prede da parte dei predatori: "))
tasso_di_mortalita_predatori = float(input("Inserire il tasso di mortalità dei predatori: "))
tasso_di_incremento_dei_predatori_attraverso_il_consumo_delle_prede = float(input("Inserire il tasso di incremento dei predatori attraverso il consumo delle prede: "))

numero_prede = int(input("Inserire il numero delle prede: "))
numero_predatori = int(input("Inserire il numero dei predatori: "))

numero_periodi = int(input("Inserire il numero di periodi: "))

x_n = numero_prede
y_n = numero_predatori

print(f"Numero prede: {x_n}\tNumero predatori: {y_n}")

for n in range(numero_periodi):
    x_n_1 = x_n*(1+tasso_di_crescita_delle_prede-(tasso_di_distruzione_delle_prede_da_parte_dei_predatori*y_n))
    y_n_1 = y_n*(1-tasso_di_mortalita_predatori+(tasso_di_incremento_dei_predatori_attraverso_il_consumo_delle_prede*x_n))

    x_n = x_n_1
    y_n = y_n_1

    print(f"Periodo: {n}\tNumero prede: {x_n}\tNumero predatori: {y_n}")



