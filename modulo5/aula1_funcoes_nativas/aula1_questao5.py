# Questão 5

import emoji

print(f"Emojis disponíveis: \n{emoji.emojize(':red_heart:')} - :red_heart: \n{emoji.emojize(':thumbs_up:')} - :thumbs_up: \n{emoji.emojize(':thinking_face:')} - :thinking_face: \n{emoji.emojize(':partying_face:')} - :partying_face:")

frase = input("Digite uma frase e ela será emojizada: ")

print(emoji.emojize(frase))