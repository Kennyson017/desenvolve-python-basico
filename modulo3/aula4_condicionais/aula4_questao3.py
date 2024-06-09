#  Questão 3

ano = int(input("Digite o ano que deseja saber se é bissexto:"))

# verifica a condição de bissexto
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
  print(ano,"é um ano bissexto!")

else:
  print(ano, "não é um ano bissexto.")