import re

nome_arquivo_frase = "frase.txt"
nome_arquivo_palavras = "palavras.txt"

with open(nome_arquivo_frase, 'r') as arquivo:
    conteudo = arquivo.read()

palavras = re.findall(r'\b[A-Za-zÀ-ÿ]+\b', conteudo)

with open(nome_arquivo_palavras, 'w') as arquivo:
    for palavra in palavras:
        arquivo.write(palavra + '\n')

with open(nome_arquivo_palavras, 'r') as arquivo:
    conteudo_palavras = arquivo.read()
    print(conteudo_palavras)