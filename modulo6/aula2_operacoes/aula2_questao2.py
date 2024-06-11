import random

num_elementos = random.randint(5, 20)

elementos = []

for i in range(num_elementos):
    valor = random.randint(1, 10)
    elementos.append(valor)

print(elementos)
print(sum(elementos))
print(sum(elementos)/len(elementos))