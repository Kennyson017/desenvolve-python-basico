frase = "Meu amor mora em Roma e me deu um ramo de flores"
objetivo =  sorted("amor")

lst_palavras = frase.lower().split(" ")

anagramas = list(filter(lambda ana: sorted(ana) == objetivo, lst_palavras))

print(anagramas)

# for palavra in lst_palavras:
#     if sorted(palavra) == objetivo:
#         print(palavra)

