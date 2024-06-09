# Questão 4

n = int(input('Valor de N: '))
maior = 0 

while n > 0:
    x = int(input('Valor de x: '))
    if x > maior:
        maior = x
    else:
        n -= 1
    
print(f"Maior: {maior}")