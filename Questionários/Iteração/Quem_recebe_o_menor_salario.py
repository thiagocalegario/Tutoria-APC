menor_salario = float('inf')
maior_salario = media = count = 0
pessoa_menor_salario = pessoa_maior_salario = str()
qt_iteracao = int(input())
if qt_iteracao > 0:
    for _ in range(qt_iteracao):
        nome,salario = input().split(',')
        salario = float(salario)
        media += salario
        count += 1
        if salario < menor_salario:
            menor_salario = salario
            pessoa_menor_salario = nome
        if salario > maior_salario:
            maior_salario = salario
            pessoa_maior_salario = nome
    print(f"{media/count:.2f}\n{pessoa_maior_salario} {maior_salario:.2f}\n{pessoa_menor_salario} {menor_salario:.2f}")
else:
    print("Não tem média\nNão tem\nNão tem")
