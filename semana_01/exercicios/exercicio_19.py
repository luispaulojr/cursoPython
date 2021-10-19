volume = float(input(
    'Informe o volume em litros para ser convertido em metros cubicos (m³): ').replace(',', '.'))

print(
    f'A conversão do volume {volume} litros para metros cubicos é: {(volume / 1000)}m³')
