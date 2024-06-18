def palindromo(texto):
    texto_filtrado = ''.join(e for e in texto if e.isalnum()).lower()
    if texto_filtrado == texto_filtrado[::-1]:
        return f'"{texto}" é palíndromo!'
    else:
        return f'"{texto}" não é palíndromo!'

    
while True:
    frase = input('Digite uma frase: ')
    if frase == "fim":
        print("Finalizado com sucesso!")
        break
    print(palindromo(frase))
