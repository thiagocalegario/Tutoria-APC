qt_iteracao = int(input())
for _ in range(qt_iteracao):
    letraAtual = str()
    numeroAtual = str()
    primeiraLetra = True  # Sinaliza que está vendo a primeira letra.
    entrada = input()
    for char in entrada:
        if char.isalpha(): #Achou uma letra
            if primeiraLetra: #Verifica se é a primeira letra
                letraAtual = char
                primeiraLetra = False
            else:
                print(letraAtual * int(numeroAtual), end='')
                letraAtual = char
                numeroAtual = str()
        else:
            numeroAtual += char
    print(letraAtual * int(numeroAtual))
