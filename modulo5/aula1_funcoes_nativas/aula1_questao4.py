# Questão 4

from datetime import datetime

data_atual = datetime.now()

data_formatada = '{:02d}/{:02d}/{}'.format(data_atual.day, data_atual.month, data_atual.year)

hora = data_atual.strftime('%H:%M')

print(f"Data: {data_formatada}")
print(f"Hora: {hora}")