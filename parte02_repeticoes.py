"""
Estrutura de repetição
"""

nome = 'Luis Paulo Lessa'
lista = [1, 2, 3, 4, 5, 6]
numeros = range(10, 30)

# for para string
for letra in nome:
    print(letra)

for numero in lista:
    print(numero)

for num in numeros:
    print(num)

qtd = int(input("Quantas repetições: "))

for n in range(0, qtd):
    print(f'Imprimindo {n + 1}')