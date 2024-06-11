import random

lista = []

for i in range(20):
    lista.append(random.randint(-10,10))

print('Lista Original:', lista)   

# lista = [-5, -2, 3, 9, -8, -6, -3, -6, -4, -9, -4, -2, 10, -6, -6, -6, 7, 3, 3, 3] #lista de teste

inicio_fatia_maior, tam_fatia_maior = 0, 0 
inicio_fatia_atual, tam_fatia_atual = 0, 0 

for i in range(len(lista)):
    if lista [i] < 0:
        tam_fatia_atual += 1
        if tam_fatia_atual == 1:
            inicio_fatia_atual = i
    else:
        if tam_fatia_atual > tam_fatia_maior:
            tam_fatia_maior = tam_fatia_atual
            inicio_fatia_maior = inicio_fatia_atual
        tam_fatia_atual = 0

print('Inicio fatia:', inicio_fatia_maior, 'Tamanho fatia:', tam_fatia_maior)
del lista [inicio_fatia_maior:inicio_fatia_maior+tam_fatia_maior]
print('Lista Editada:', lista)