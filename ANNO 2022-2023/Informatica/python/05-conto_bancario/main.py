saldo = 1000
numero_di_anni = 3
tasso_di_interesse_percentuale_annuale = 5

for _ in range(numero_di_anni):
    saldo = saldo + saldo*(tasso_di_interesse_percentuale_annuale/100)

print(saldo)