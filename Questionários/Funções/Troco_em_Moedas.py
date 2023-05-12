def troco(arg):
    arg = int(arg)
    print(f"{arg//50} moedas de 50 centavos")
    arg = arg % 50
    print(f"{arg//25} moedas de 25 centavos")
    arg = arg % 25
    print(f"{arg//10} moedas de 10 centavos")
    arg = arg % 10
    print(f"{arg//5} moedas de cinco centavos")
    arg = arg % 5
    print(f"{arg} moedas de 1 centavo")