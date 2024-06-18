import random

def embaralhar_palavras(frase):
    palavras = frase.split()
    frase_embaralhada = []

    for palavra in palavras:
        if len(palavra) > 2:
            letras_internas = list(palavra[1:-1])
            random.shuffle(letras_internas)
            palavra_embaralhada = palavra[0] + ''.join(letras_internas) + palavra[-1]
            frase_embaralhada.append(palavra_embaralhada)
        else:
            frase_embaralhada.append(palavra)

    return ' '.join(frase_embaralhada)

# frase = "Python é uma linguagem de programação" # frase teste

frase =  input('Digite uma frase:')
resultado = embaralhar_palavras(frase)
print(resultado)

