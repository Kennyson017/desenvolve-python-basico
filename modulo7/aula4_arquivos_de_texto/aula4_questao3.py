import re

nome_arquivo_estomago = "estomago.txt"

with open(nome_arquivo_estomago, 'r', encoding='latin-1') as arquivo:
    linhas = arquivo.readlines()

print("Primeiras 25 linhas:")
for linha in linhas[:25]:
    print(linha, end='')

num_linhas = len(linhas)
print(f"\nNúmero de linhas do arquivo: {num_linhas}")

linha_maior = max(linhas, key=len)
print(f"Linha com maior número de caracteres: {linha_maior.strip()}")

menções_nonato = sum(1 for linha in linhas if re.search(r'\bNonato\b', linha, re.IGNORECASE))
menções_iria = sum(1 for linha in linhas if re.search(r'\bÍria\b', linha, re.IGNORECASE))

print(f"Número de menções a 'Nonato': {menções_nonato}")
print(f"Número de menções a 'Íria': {menções_iria}")
