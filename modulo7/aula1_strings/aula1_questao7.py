import random

def encrypt(c, key, minchr=33, maxchr=127):
    nc = ord(c) + key
    return chr(nc) if nc < maxchr else chr(minchr + (nc % maxchr))

nomes = ["Luana", "Ju", "Davi", "Vivi", "Pri", "Luiz"]
key = random.randint(1,10)

nomes_crypt = []
for nome in nomes:
    nome_crypt = ''.join(map(lambda c: encrypt(c, key), nome))
    nomes_crypt.append(nome_crypt)

print(f"Nomes: {nomes} \nChave: {key} \nCriptografia: {nomes_crypt}")

