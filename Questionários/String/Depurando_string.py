def não_possui_a_letra_u(palavra):
    letraU='Uuúüùûū'
    for letra in palavra:
        if letra in letraU:
            return False
    return True