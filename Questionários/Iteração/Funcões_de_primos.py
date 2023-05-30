def ehPrimo(num):                            #RECEBE NUM PARA VERIFICAR SE É PRIMO
    count = 0                                #VARIVAVEL CONTADOR, PARA ARMAZENAR A QUANTIDADE DE DIVISORES
    for i in range(1, num):                  #PARA 1 ATÉ NUM
        if num % i == 0:                     #SE O RESTO DE NUM POR I É ZERO (I É UM DIVISOR)
            count += 1                       #COUNTADOR +1, ACHOU UM DIVISOR
    if count <= 1:                           #SE VOCÊ ACHOU SOMENTE 1 DIVISOR, OU SEJA, O 1
        return 1                             #RETORNA 1, O NUMERO É PRIMO
    else:                                    #SE TIVER MAIS DE 1 DIVISOR
        return 0                             #RETORNA ZERO, NÅO É PRIMO

def divisoresPrimos(num):                    #CALCULA QUANTOS DIVISORES PRIMOS TEM UM NUMERO
    count = -1                               #COUNT -1, POIS INICIAREMOS DEPOIS DO ZERO
    for i in range(1,num):                   #PARA 1 ATE NUM
        if num % i == 0 and ehPrimo(i):      #SE O RESTO DE NUM POR I == 0 (DIVISOR) E EHPRIMO(I) == 1
            count += 1                       #ACHOU UM DIVISOR PRIMO
    return count                             #RETORNA QUANTIDADE DE DIVISORES PRIMOS


