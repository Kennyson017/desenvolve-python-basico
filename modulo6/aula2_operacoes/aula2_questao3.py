import random

lista1, lista2 = list(), []
interseccao = list()

for i in range(20):
    valor1, valor2 = random.randint(0, 50), random.randint(0, 50)
    lista1.append(valor1)
    lista2.append(valor2)
    # if valor1 == valor2:
    #     interseccao.append(valor1)

for elemento in lista1:
    if elemento in lista2 and elemento not in interseccao:
        interseccao.append(elemento)

print('lista 1: ', lista1)
print('lista 2: ', lista2)
print('Intersecção: ', sorted(interseccao))

interseccao.sort()
for i in interseccao:
    print(f"{i}: ({lista1.count(i)}, {lista2.count(i)})")
