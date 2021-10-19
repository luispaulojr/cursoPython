volume = float(input(
    'Informe o volume em metros cubicos (m³) para ser convertido em litros: ').replace(',', '.'))

print(
    f'A conversão do volume {volume}m³ para litros é: {(volume * 1000)} litros')
