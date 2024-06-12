# frase = "Meu amor mora em Roma e me deu um ramo de flores" # Frase teste

frase = input("Digite uma frase: ")
vogais = "aeiou"

contagem = list(filter(lambda letra: letra in vogais, frase.lower()))
indices = list(filter(lambda indice: frase[indice].lower() in vogais, range(len(frase))))

print(len(contagem), 'Vogais')
print('Indices', indices)