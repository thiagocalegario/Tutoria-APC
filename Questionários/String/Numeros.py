entrada = input()
count = 0
for _ in entrada:
    if _.isnumeric():
        count += 1
print(count)