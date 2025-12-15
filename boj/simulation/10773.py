n = int(input())
lis = []

for i in range(n):
    num = int(input())

    if num == 0:
        lis.pop()
    else:
        lis.append(num)

print(sum(lis))