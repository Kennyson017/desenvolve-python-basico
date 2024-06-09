# Questão 6

n = int(input('Quantidade de Experimentos: '))
cont = 0

sapos = 0
coelhos = 0
ratos = 0

while cont < n:
    n_cobaias = int(input("Nº de cobaias: "))
    tipo_cobaia = input("Tipo de cobaia (S, R ou C): ")
    print(n_cobaias, tipo_cobaia)

    if tipo_cobaia == "S" or tipo_cobaia == "s":
        sapos += n_cobaias
    elif tipo_cobaia == "R" or tipo_cobaia == 'r':
        ratos += n_cobaias
    elif tipo_cobaia == "C" or tipo_cobaia == 'c':
        coelhos += n_cobaias
    
    cont += 1

    total = coelhos + ratos + sapos

print(f"Total: {coelhos+ratos+sapos} \nTotal de Coelhos: {coelhos} \nTotal de Ratos: {ratos} \nTotal de Sapos: {sapos}")
print(f"Porcentagem de Coelhos: {(coelhos*total)/100:.2f}% \nPorcentagem de Ratos: {(ratos*total)/100:.2f}% \n Porcentagem de Sapos: {(sapos*total)/100:.2f}% ")