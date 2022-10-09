"""
Un codice alfanumerico lungo 16 caratteri che alterni le stringhe “abcd” e “1234”.
"""

import random


codice = ""
stringhe = ["abcd", "1234"]


for _ in range(int(16/4)):
    codice += random.choice(stringhe)

print(codice)