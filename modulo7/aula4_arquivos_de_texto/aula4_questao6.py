import csv

# Nome do arquivo CSV
nome_arquivo_spotify = "spotify-2023.csv"

# Dicionário para armazenar a música mais tocada de cada ano
musicas_mais_tocadas = {}

# Lê o arquivo CSV
with open(nome_arquivo_spotify, 'r', encoding='latin-1') as arquivo_csv:
    leitor_csv = csv.reader(arquivo_csv)
    next(leitor_csv)  # Pula o cabeçalho

    for linha in leitor_csv:
        track_name = linha[0]
        artist_name = linha[1]
        artist_count = int(linha[2])
        released_year = int(linha[3])
        streams = int(linha[8])

        # Verifica se o ano está no intervalo desejado
        if 2012 <= released_year <= 2022:
            # Verifica se a música deve ser atualizada no dicionário
            if released_year not in musicas_mais_tocadas or streams > musicas_mais_tocadas[released_year][3]:
                musicas_mais_tocadas[released_year] = [track_name, artist_name, released_year, streams]

# Converte o dicionário para uma lista ordenada pelos anos
lista_musicas = [musicas_mais_tocadas[ano] for ano in sorted(musicas_mais_tocadas)]

# Imprime a lista de músicas mais tocadas
print(lista_musicas)
