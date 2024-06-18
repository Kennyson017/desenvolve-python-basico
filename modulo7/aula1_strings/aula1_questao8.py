def calcular_digito_verificador(cpf_base):
    multiplicador = 2
    soma = 0

    # Calcula o primeiro dígito verificador
    for digito in reversed(cpf_base):
        soma += int(digito) * multiplicador
        multiplicador += 1

    resto = soma % 11
    digito_verificador = 0 if resto < 2 else 11 - resto

    return digito_verificador

def validar_cpf(cpf):
    # Remove pontos e traço do CPF
    cpf_numeros = ''.join(filter(str.isdigit, cpf))

    # Verifica se o CPF possui 11 dígitos
    if len(cpf_numeros) != 11:
        return print('CPF não possui 11 digitos! Algo deu errado, tente novamente!')

    # Calcula os dígitos verificadores
    primeiro_digito = calcular_digito_verificador(cpf_numeros[:9])
    segundo_digito = calcular_digito_verificador(cpf_numeros[:9] + str(primeiro_digito))

    # Verifica se os dígitos fornecidos são válidos
    if cpf_numeros[-2:] == f"{primeiro_digito}{segundo_digito}":
        return print('CPF válido!')
    else:
        return print('CPF inválido!')

cpf_input = input("Digite o CPF na forma XXX.XXX.XXX-XX: ")

validar_cpf(cpf_input)
