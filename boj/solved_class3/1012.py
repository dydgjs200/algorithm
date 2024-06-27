import sys

n, m = map(int, input().split(" "))
lis = [[0 for _ in range(n+1)] for _ in range(n+1)]
minVal = sys.maxsize

for _ in range(m):
    a, b = map(int, input().split(" "))

    lis[a][b] = lis[b][a] = 1