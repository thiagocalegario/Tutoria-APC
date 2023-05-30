entrada = input()
word_to_replace = input()
if word_to_replace in entrada:
    print(entrada.replace(word_to_replace, '*'))
else:
    print('tudo certo :)')