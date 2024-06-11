# Questão 3

import random

valor = random.randint(0, 10)

while True:
    n_user = int(input("Adivinhe o número entre 1 e 10: "))

    if valor == n_user:
        print(f"Correto! O número é {valor}.")
        break
    elif valor < n_user:
        print("Muito alto, tente novamente!")
    elif valor > n_user:
        print("Muito baixo, tente novamente!")

print("Parabéns você conseguiu!!!")
