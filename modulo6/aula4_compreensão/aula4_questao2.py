# 2) Solicite uma frase do usuário e usando compreensão de listas imprima:
# A lista de vogais da frase, ordenada alfabeticamente
# A lista de consoantes da frase
# Exemplo:
# Digite uma frase: Eu gosto de programar em Python
# Vogais: ['a', 'a', 'e', 'e', 'o', 'o', 'o', 'o', 'u']
# Consoantes: ['E', 'g', 's', 't', 'd', 'p', 'r', 'g', 'r', 'm', 'r', 'm', 'P', 'y', 't', 'h', 'n'].

frase = input('Escreva uma frase: ')
vogais = 'aeiouAEIOU'

lista_vogais = sorted(n for n in frase if n in vogais)
lista_consoantes = sorted([n for n in frase if n.isalpha() and n not in vogais])

print(frase)
print(lista_vogais)
print(lista_consoantes)


