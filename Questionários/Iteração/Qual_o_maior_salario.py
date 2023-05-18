maior_salario = 0
while True:
    nome,salario = input().split(',')
    salario = float(salario)
    if nome == "Fim":
        break
    if salario > maior_salario:
        maior_salario = salario
print(f"{maior_salario:.2f}") if maior_salario > 0 else print('Não tem')