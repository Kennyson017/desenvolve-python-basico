# Exercício 3

nome_produto1 = input('Digite o nome do produto 1: ')
preco_unid1 = float(input('Digite o preço unitário do produto 1: '))
qtd1 = int(input('Digite a quantidade do produto 1: '))

nome_produto2 = input('Digite o nome do produto 2: ')
preco_unid2 = float(input('Digite o preço unitário do produto 2: '))
qtd2 = int(input('Digite a quantidade do produto 2: '))

nome_produto3 = input('Digite o nome do produto 3: ')
preco_unid3 = float(input('Digite o preço unitário do produto 3: '))
qtd3 = int(input('Digite a quantidade do produto 3: '))

total_p1 = preco_unid1 * qtd1
total_p2 = preco_unid2 * qtd2
total_p3 = preco_unid3 * qtd3

total_geral = total_p1 + total_p2 + total_p3

print(f"Total: R${total_geral:,.2f}")