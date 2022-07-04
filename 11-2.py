n = input()

result = int(n[0])

for i in (1, len(n)):
    if int(n[i]) <= 1 or result <= 1:
        reuslt += n[i]
    else:
        result *= n[i]

print(result)