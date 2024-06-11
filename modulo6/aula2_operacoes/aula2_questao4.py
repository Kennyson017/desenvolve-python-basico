
lista1, lista2 = [], []

n1 = int(input("Digite a quantidade de elementos da lista 1: "))
print(f"Digite os {n1} elementos da lista 1: ")

for i1 in range(1, n1+1):
    lista1.append(input(f"Digite o {i1}º elemento da lista 1: "))

n2 = int(input("Digite a quantidade de elementos da lista 2: "))
print(f"Digite os {n2} elementos da lista 2: ")

for i2 in range(1, n2+1):
    lista2.append(input(f"Digite o {i2}º elemento da lista 2: "))

intercalada = []
cont1, cont2 = 0, 0

while cont1 < n1 and cont2 < n2:
    intercalada.append(lista1[cont1])
    cont1 += 1
    intercalada.append(lista2[cont2])
    cont2 += 1

while cont1 < n1:
    intercalada.append(lista1[cont1])
    cont1 += 1

while cont2 < n2:
    intercalada.append(lista2[cont2])
    cont2 += 1

print(f"Lista 1: {lista1}")
print(f"Lista 2: {lista2}")
print(f"Lista Intercalada: {intercalada}")

