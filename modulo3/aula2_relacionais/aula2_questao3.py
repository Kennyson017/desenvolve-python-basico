# Questão 3

idade = int(input("Digite sua idade: "))
jogos = input("Já jogou pelo menos 3 jogos de tabuleiro? ") == 'true'
vitorias = int(input("Quantos jogos já venceu? "))

aptidao = (idade >=16 and idade<=18) and jogos and (vitorias >= 1)

print("Apto para ingressar no clube de jogos de tabuleiro: ", aptidao)