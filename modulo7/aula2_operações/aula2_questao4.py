import re

def validador_senha(senha):
    # Pelo menos 8 caracteres de comprimento.
    if len(senha) < 8:
        return False
    
    # Contém pelo menos uma letra maiúscula e uma letra minúscula.
    if not re.search(r"[a-z]", senha) or not re.search(r"[A-Z]", senha):
        return False
    
    # Contém pelo menos um número.
    if not re.search(r"\d", senha):
        return False
    
    # Contém pelo menos um caractere especial (por exemplo, @, #, $).
    if not re.search(r"[!@#$%^&*()-_=+{};:,<.>/?\\|~]", senha):
        return False
    
    return True

senha1 = "Senha123@"
senha2 = "senhafraca"
senha3 = "Senha_fraca"

print(validador_senha(senha1)) 
print(validador_senha(senha2))  
print(validador_senha(senha3))  