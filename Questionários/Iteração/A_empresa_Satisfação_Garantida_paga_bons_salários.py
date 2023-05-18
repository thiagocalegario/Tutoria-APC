count = 0
salario_total = 0
while True:
    nome,salario = input().split(',')
    salario = float(salario)
    if nome == "Fim":
        break
    count += 1
    salario_total += salario
print(f"{salario_total/count:.2f}") if salario_total > 0 else print('0.00')