def dec2hex4bits(x):
    if x < 10:
        return str(x)
    elif x == 10:
        return 'A'
    elif x == 11:
        return 'B'
    elif x == 12:
        return 'C'
    elif x == 13:
        return 'D'
    elif x == 14:
        return 'E'
    elif x == 15:
        return 'F'


def dec2hex8bits(x):
    mais_significativo = x // 16
    menos_significativo = x % 16
    return dec2hex4bits(mais_significativo) + dec2hex4bits(menos_significativo)


cor, red, green, blue = input().split(sep=',')
red = int(red)
green = int(green)
blue = int(blue)
print(f'{cor} #{dec2hex8bits(red)}{dec2hex8bits(green)}{dec2hex8bits(blue)}')
