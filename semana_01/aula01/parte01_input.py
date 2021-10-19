"""
Função input
"""

nome = input('Digite seu nome: ')

# padrao classico de impressão
print('Seu nome é ' + nome)
# padrao like javascript
print('Seu nome é', nome)
# padrao classico de python 3.0
print('Seu nome é %s' % nome)
# padrao classico de python 3.0
print('Seu nome é {}'.format(nome))
# padrao classico de python 3.7
print(f'Seu nome é {nome}')