
from collections import Counter

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

texto = """
Verdades da Profissão de Professor
Ninguém nega o valor da educação e que um bom professor é imprescindível. Mas, ainda que desejem bons professores para seus filhos, poucos pais desejam que seus filhos sejam professores. Isso nos mostra o reconhecimento que o trabalho de educar é duro, difícil e necessário, mas que permitimos que esses profissionais continuem sendo desvalorizados. Apesar de mal remunerados, com baixo prestígio social e responsabilizados pelo fracasso da educação, grande parte resiste e continua apaixonada pelo seu trabalho.
A data é um convite para que todos, pais, alunos, sociedade, repensemos nossos papéis e nossas atitudes, pois com elas demonstramos o compromisso com a educação que queremos. Aos professores, fica o convite para que não descuidem de sua missão de educar, nem desanimem diante dos desafios, nem deixem de educar as pessoas para serem “águias” e não apenas “galinhas”. Pois, se a educação sozinha não transforma a sociedade, sem ela, tampouco, a sociedade muda.
"""

palavras = texto.split()
print(palavras)
print(Counter(palavras))

