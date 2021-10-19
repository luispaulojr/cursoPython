import math

graus = float(input(
    'Informe o ângulo em graus para ser convertido em radianos: ').replace(',', '.'))

print(
    f'A conversão do ângulo {graus} em graus para radianos é: {(graus * (math.pi / 180))}')