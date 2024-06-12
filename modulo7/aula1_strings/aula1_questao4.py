tel = input('Digite o número: ')

if len(tel) == 8:
    nono_digito = "9"
    tel = nono_digito + tel
    tel = tel[:5] + "-" + tel[5:10]
    print(f"Número completo: {tel}")

elif len(tel) == 9:
    tel = tel[:5] + "-" + tel[5:10]
    print(f"Número completo: {tel}")

else:
    print("Número Inválido! Tente novamente")

