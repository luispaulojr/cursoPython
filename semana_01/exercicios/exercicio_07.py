temperatura = float(input(
    'Informe a temperatura em Fahrenheit para ser convertida: ').replace(',', '.'))

print(
    f'A conversão de {temperatura} em Fahrenheit para Celsius é: {(5 * (temperatura - 32)/9)} °C')