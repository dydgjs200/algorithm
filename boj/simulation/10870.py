num = int(input())
lis = [0,1]

if num == 0:
    print(0)
elif num == 1:
    print(1)
else:
    for i in range(2, num + 1):
        lis.append(lis[i - 2] + lis[i - 1])

    print(lis[-1])