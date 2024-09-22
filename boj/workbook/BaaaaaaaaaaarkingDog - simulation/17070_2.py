# dfs
# 가로 = 가로, 대각선
# 세로 = 세로, 대각선
# 대각선 = 가, 세, 대각선

# visit는 필요 없음 -> n, n으로 가는 방법밖에 없기 때문

def dfs(y, x, pipe):        # pipe = 0,1,2 -> 가로, 세로, 대각선
    global cnt

    if y == n-1 and x == n-1:
        cnt += 1
        return

    if pipe == 0:
        if x+1 < n and lis[y][x+1] == 0:
            dfs(y, x+1, 0)
        if x+1 < n and y+1 < n and lis[y+1][x] == 0 and lis[y+1][x+1] == 0 and lis[y][x+1] == 0:
            dfs(y+1, x+1, 2)
    if pipe == 1:
        if y+1 < n and lis[y+1][x] == 0:
            dfs(y+1, x, 1)
        if x+1 < n and y+1 < n and lis[y+1][x] == 0 and lis[y+1][x+1] == 0 and lis[y][x+1] == 0:
            dfs(y+1, x+1, 2)
    if pipe == 2:
        if x+1 < n and lis[y][x+1] == 0:
            dfs(y, x+1, 0)
        if y+1 < n and lis[y+1][x] == 0:
            dfs(y+1, x, 1)
        if x+1 < n and y+1 < n and lis[y+1][x] == 0 and lis[y+1][x+1] == 0 and lis[y][x+1] == 0:
            dfs(y+1, x+1, 2)


import sys

input = sys.stdin.readline
n = int(input())
lis = []
cnt = 0

for _ in range(n):
    lis.append(list(map(int, input().split(" "))))

dfs(0,1,0)

print(cnt)