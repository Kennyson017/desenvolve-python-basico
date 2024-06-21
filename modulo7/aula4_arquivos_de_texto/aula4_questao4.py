import random

def imprime_enforcado(erros):
    with open("gabarito_enforcado.txt", 'r') as arquivo:
        estagios = arquivo.read().split('\n\n')
    print(estagios[erros])

with open("gabarito_forca.txt", 'r') as arquivo:
    palavras = arquivo.read().splitlines()

palavra = random.choice(palavras)
palavra_oculta = ['_' for _ in palavra]

tentativas = 6
erros = 0

while erros < tentativas and '_' in palavra_oculta:
    print(" ".join(palavra_oculta))
    letra = input("Digite uma letra: ").lower()
    
    if letra in palavra.lower():
        for i, char in enumerate(palavra.lower()):
            if char == letra:
                palavra_oculta[i] = palavra[i]
    else:
        erros += 1
        imprime_enforcado(erros)

if '_' not in palavra_oculta:
    print("Parabéns, você adivinhou a palavra!")
else:
    print(f"Você perdeu! A palavra era: {palavra}")
