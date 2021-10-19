temperatura = float(input(
    'Informe a temperatura em Kelvin para ser convertida: ').replace(',', '.'))

print(
    f'A conversão de {temperatura} em Kelvin para Celsius é: {(temperatura - 273.15)} °C')