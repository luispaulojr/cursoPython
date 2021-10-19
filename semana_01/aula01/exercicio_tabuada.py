"""
Exercício Tabuada
"""

print('Tabuada!')

num01 = range(1, 11)
num02 = range(1, 11)

for n1 in num01:
    print(f"\nTabuada de {n1}")
    for n2 in num02:
        print(f"Tabuada de {n1} x {n2} = {n1 * n2}")