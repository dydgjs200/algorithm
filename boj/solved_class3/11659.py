import sys
input = sys.stdin.readline

n, m = map(int, input().split(" "))
lis = list(map(int, input().split(" ")))
sumLis = [0] * (n+1)
sumLis[1] = lis[1]

for i in range(1, n+1):
    sumLis[i] = lis[i-1] + sumLis[i-1]

for _ in range(m):
    a, b = map(int, input().split(" "))

    print(sumLis[b] - sumLis[a-1])
