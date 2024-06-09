# Questão 5

n = int(input("Número de respondentes: "))
cont = 0
soma = 0

while cont < n:
    idade = int(input('Idade: '))
    soma += idade
    cont += 1

media = soma / n

print(f'A média das idades é {media}')