# Questão 5

genero = input('Genero: ')
idade = int(input('Idade: '))
tempo = int(input('Tempo de Trabalho: '))

# A: Para mulheres, ter mais de 60 anos. Para homens, 65.
# B: Ou ter trabalhado pelo menos 30 anos
# C: Ou ter 60 anos  e trabalhado pelo menos 25.

a = (genero == 'f' and idade >= 60) or (genero == 'm' and idade >= 65)
b = tempo > 30
c = idade >= 60 and tempo >= 25

aposentadoria = a or b or c

print(aposentadoria)