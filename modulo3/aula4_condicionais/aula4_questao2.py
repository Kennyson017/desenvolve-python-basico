#  Questão 2

filme = input('Filme assistido: ')
avaliacao = int(input('Avalie o Filme em uma escala de 1 a 5: '))

if avaliacao == 5:
    comentario = "Excelente!"

elif avaliacao == 4:
    comentario = "Muito Bom!"

elif avaliacao == 3:
    comentario = "Bom!"

elif avaliacao == 2:
    comentario = "Regular."

elif avaliacao == 1:
    comentario = "Ruim."

print(f'O filme "{filme}" foi avaliado como {comentario}')