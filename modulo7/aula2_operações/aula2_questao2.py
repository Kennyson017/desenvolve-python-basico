frase = input("Digite uma frase: ")

vogais = "AEIOUaeiou"

for vogal in vogais:
    frase = frase.replace(vogal, '*')

print(frase)


