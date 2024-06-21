import csv

# Lista de livros
livros = [
    ["Título1", "Autor1", 2001, 300],
    ["Título2", "Autor2", 2002, 350],
    # Adicione mais livros aqui
]

# Nome do arquivo CSV
nome_arquivo_csv = "meus_livros.csv"

# Cria e escreve no arquivo CSV
with open(nome_arquivo_csv, 'w', newline='') as arquivo_csv:
    escritor_csv = csv.writer(arquivo_csv)
    escritor_csv.writerow(["Título", "Autor", "Ano de publicação", "Número de páginas"])
    escritor_csv.writerows(livros)

print(f"Arquivo {nome_arquivo_csv} criado com sucesso.")
