print('+--------------------+--------------------+')
print('|        peixe       |      preço   R$    |')
print('+--------------------+--------------------+')
menor_preco = float('inf')
menor_preco_nome = str()
count = 0
string1 = 'Hoje não tem peixe'
string2 = 'Cambada de menor preço'
while True:
    peixe, preco = input().split()
    preco = float(preco)
    if peixe == 'fim':
        if count == 0:
            print(f'|{string1:^41}|')
            print('+-----------------------------------------+')
        elif count > 1:
            print()
            print('+-----------------------------------------+')
            print(f'|{string2:^41}|')
            print('+--------------------+--------------------+')
            print(f"| {menor_preco_nome:<19}|{menor_preco:>19.2f} |")
            print('+--------------------+--------------------+')


        break
    if preco < menor_preco:
        menor_preco = preco
        menor_preco_nome = peixe
    count += 1
    print(f"| {peixe:<19}|{preco:>19.2f} |")
    print('+--------------------+--------------------+')
