import math

radiano = float(input(
    'Informe o ângulo em radianos para ser convertido em graus: ').replace(',', '.'))

print(
    f'A conversão do ângulo {radiano} em radianos para graus é: {(radiano * (180 / math.pi))}')