entrada = input()
for _ in range(1, len(entrada),2):
    if entrada[_] != ' ':
        print(entrada[_], end="")