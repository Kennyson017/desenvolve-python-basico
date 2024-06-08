# Exercício 1

comprimento = float(input('Comprimento do terreno: '))
largura = float(input('Largura do terreno: '))
preço_m = float(input('Valor do metro quadrado: '))

area = comprimento * largura

valor_terreno = area * preço_m

print(f"O terreno possui {area}m2 e custa R${valor_terreno:,.2f}")