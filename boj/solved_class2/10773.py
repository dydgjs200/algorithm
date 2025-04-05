n = int(input())
lis = []

for i in range(n):
    number = int(input())

    if len(lis) == 0 and number == 0:
        continue
    else:
        if number == 0:
            lis.pop()
        else:
            lis.append(number)

print(sum(lis))