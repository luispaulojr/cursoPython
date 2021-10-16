"""
string
"""

nome = "Luis estuda Python\nAos sábados de tarde\n\tpelo Senac"
print(nome)

print(nome.upper())

texto = "A AULA DE SENAC ESTÁ FLUINDO"
print(texto.lower())

empresa = 'SENAC AARJ - CURSO PYTHON'

print(empresa[6:10]) 

"""
[x:y]
x -> é o caractere inicial, que vai de 0 a N, onde 0 é o primeiro caracter e N é o último caracter da string
y -> é o caractere "até" que deseja atingir. Lembrando que se esse valor for menor que o caracter incial nao ira mostar nada, pois estará "atras" do caracter inicial
"""

# detalhamento da class string
print(dir(nome))

# inverter uma string
print(empresa[::-1])

# replace em uma string
print(empresa.replace('E', 'Z'))