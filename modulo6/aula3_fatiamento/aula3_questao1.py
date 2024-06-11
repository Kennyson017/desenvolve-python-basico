
lista = []

print('Digite "0" quando quiser encerrar.')
while True:
    n = int(input("Digite um valor: "))
    if n == 0:
        print('lista encerrada.')
        break # Se N igual a 0 termina o codigo
    lista.append(n)

# lista = [10, 56, 45, 78, 98, 32, 4, 2]

print(lista) # original
print(lista[:3]) # 3 primeiros elementos
print(lista[-2:len(lista)]) # 2 ultimos elementos
print(lista[::-1]) # invertida
print(lista[::2]) # Indices pares
print(lista[1::2]) # Indices inpares


