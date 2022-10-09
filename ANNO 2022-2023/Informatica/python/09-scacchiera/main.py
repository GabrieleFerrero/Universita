"""
Una scacchiera di dimensioni 5x5 in cui le caselle bianche sono rappresentate da “0”, e le
caselle nere da “1”.
"""

casella=0
scacchiera=""
for _ in range(5):
    for _ in range(5):
        scacchiera += str(casella)
        if casella==0: casella=1
        else: casella=0
    scacchiera += "\n"

print(scacchiera)