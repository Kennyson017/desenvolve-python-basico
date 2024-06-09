# Questão 4

peso_kg = float(input('Peso do produto em Kg: '))
distancia_km = float(input('Distância em Km: '))

if distancia_km <= 100:
    preco_entrega = 1 * peso_kg

elif (distancia_km >= 100) and (distancia_km <= 300):
    preco_entrega = 1.5 * peso_kg

elif distancia_km > 300:
    preco_entrega = 2 * peso_kg

if peso_kg > 10:
    preco_entrega = preco_entrega + 10  # taxa acima de 10kg

print(f'O preço da entrega é R${preco_entrega:,.2f}')