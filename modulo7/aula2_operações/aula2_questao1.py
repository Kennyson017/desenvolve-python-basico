mes_text = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
mes_number = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]

nascimento = input('Digite uma data de nascimento(dd/mm/aaaa): ')

data_separada = nascimento.split('/')
index_mes_text = mes_number.index(data_separada[1])

print(f"Você nasceu em {data_separada[0]} de {mes_text[index_mes_text]} de {data_separada[2]}")