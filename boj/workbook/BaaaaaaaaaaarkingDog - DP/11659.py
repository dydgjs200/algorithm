import sys
input = sys.stdin.readline

n, m = map(int, input().split(" "))
lis = list(map(int, input().split(" ")))
sumLis = [lis[0]]

for i in range(1, len(lis)):
    sumLis.append(lis[i] + sumLis[-1])

for _ in range(m):
    a, b = map(int, input().split(" "))

    if a == 1:
        print(sumLis[b-1])
    else:
        print(sumLis[b-1] - sumLis[a-2])
