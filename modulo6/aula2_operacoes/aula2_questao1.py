import random

lista = list()

for i in range(20): 
    valor_aleatorio = random.randint(-100, 100)
    lista.append(valor_aleatorio)

print(f"Lista ordenada: {sorted(lista)}")
print(f"Lista original {(lista)}")
print(f"Indice: {lista.index(max(lista))} Valor: {max(lista)}")
print(f"Indice: {lista.index(min(lista))} Valor: {min(lista)}")
