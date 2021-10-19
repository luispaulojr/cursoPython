# https://www.metric-conversions.org/pt-br/peso/quilogramas-em-libras.htm

massa = float(input(
    'Informe o valor da massa em quilogramas para ser convertido em libras: ').replace(',', '.'))

print(
    f'A conversão da massa {massa}kg para libras é: {(massa * 2.2046)} lb')
