"""
Scrivere un programma che prende in input un numero intero x e
visualizza a schermo le seguenti espressioni, accompagnate dai loro valori di verità. Testare il
programma con numerosi valori di x.
I. x > 0 and x < 100
II. x > 0 or x < 100
III. x > 0 or 100 < x
IV. x > 0 and x < 100 or x == -1
"""

x = int(input("Inserire numero: "))

print(f"x > 0 and x < 100: {x > 0 and x < 100}")
print(f"x > 0 or x < 100: {x > 0 or x < 100}")
print(f"x > 0 or 100 < x: {x > 0 or 100 < x}")
print(f"x > 0 and x < 100 or x == -1: {x > 0 and x < 100 or x == -1}")