# Questão 4

personagem = input('Escolha a classe (guerreiro, mago ou arqueiro): ')
força = int(input('Digite os pontos de força (de 1 a 20): '))
magia = int(input('Digite os pontos de magia (de 1 a 20): '))

guerreiro = força >= 15 and magia <= 10
mago = força <= 10 and magia >= 15
arqueiro =  (força > 5 and força <= 15) and (magia > 5 and magia <= 15)

atributos = (personagem == 'guerreiro' and guerreiro) or (personagem == 'mago' and mago) or (personagem == 'arqueiro' and arqueiro)

print('Pontos de atributo consistentes com a classe escolhida: ', atributos) 