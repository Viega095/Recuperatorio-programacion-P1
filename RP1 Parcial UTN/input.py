def validar_str(palabra:str) -> bool:
    if len(palabra) < 3:
        return False
    
    for letras in palabra:
        codigo = ord(letras)
        if not ((65 <= codigo <= 90) or (97 <= codigo <= 122) or codigo == 32 or codigo == 164 or codigo == 165):
            return False
    return True


def validar_numeros(numero:str) -> bool:
    for numeros in numero:
        codigo = ord(numeros)
        if not (48 <= codigo <= 57):
            return False
        return True

