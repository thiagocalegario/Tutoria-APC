palavra = input()
cont = 0
tamanho = len(palavra) - 1

for i in range(len(palavra) // 2):
    if palavra[i] != palavra[tamanho - i]:
        cont += 1

if palavra == palavra[::-1] and len(palavra) % 2 == 0:
    print("OFF")
else:
    if cont <= 1:
        print("ON")
    else:
        print("OFF")