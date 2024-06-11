# Questão 2

import random, math

n = int(input("Digite a quantidade de valores: "))
soma = 0

for i in range(1, n+1):
    valor = random.randint(0, 100)
    print(f"{i}º: {valor}")
    soma += valor

print(f'Soma: {soma}')
print(f"A raiz quadrada da soma é: {math.sqrt(soma):.2f}")