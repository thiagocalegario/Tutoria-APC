x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
D = (((x2-x1) ** 2) + ((y2-y1) ** 2)) ** (1/2)
if D <= 100:
    print("É o amor da minha vida!")
elif 100 < D and D <= 200:
    print("Talvez dê certo")
else:
    print("Não vale a pena investir")