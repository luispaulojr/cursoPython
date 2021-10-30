"""
    Tuplas são imutáveis
    arrays - listas são mutáveis
    [] utilizado para declaração de lista
    () utilizado para declaração de tupla
"""

"""
# declaração de uma tupla utilizando parenteses
"""
tupla1 = (1, 2, 3, 4, 5, 6)
print(tupla1)

"""
# declaração de uma tupla não utilizando parenteses
"""
tupla2 = 1, 2, 3, 4, 5, 6
print(type(tupla2))

"""
# a tupla pode ser heterogêneco
"""
tupla3 = (4, 'senac')
print(type(tupla3[0]))
print(type(tupla3[1]))
print(type(tupla3))

# desempacotamento
tupla4 = 'Curso de python', 'para os melhores professores'
curso, elogio = tupla4

print(curso)
print(elogio)

"""
# a tupla pode ser heterogêneco
"""
tupla5 = (1, 2, 3, 4, 5, 6)
print(sum(tupla5))
print(max(tupla5))
print(min(tupla5))
print(len(tupla5))

"""
# a tupla pode ser incrementada
"""
tupla6 = 23, 10, 2021
tupla6 += 'Python',
print(tupla6)