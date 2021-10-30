"""
# declaração do array
"""
cores = ['verde', 'amarelo', 'azul', 'branco']
print(cores[0])

"""
# for básico
"""
for cor in cores:
    print(cor)

"""
# utilizando contador e usando a função len() para coletar o tamanho(size) da lista
"""
indice = 0
while indice < len(cores):
    print(cores[indice])
    indice += 1

"""
# utilizando o enumerate para definição do indice
"""
for indice, cor in enumerate(cores):
    print(indice, cor)


"""
# utilizando controle de fluxo
"""
carrinho = []
produto = []

while produto != 'sair':
    print("Adicione o produto na lista ou 'sair' para sair")
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)

for produto in carrinho:
    print(produto)