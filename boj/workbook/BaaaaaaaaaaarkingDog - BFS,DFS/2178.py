from collections import deque
import sys

mx = [1, -1, 0, 0]
my = [0, 0, -1, 1]

def bfs(y, x, visit):
    que = deque()
    que.append((y,x))
    visit[y][x] = 1

    while que:
        ty, tx = que.popleft()

        if ty == n-1 and tx == m-1:
            return

        for i in range(4):
            dy = my[i] + ty
            dx = mx[i] + tx

            if 0 <= dy < n and 0 <= dx < m:
                if not visit[dy][dx] and lis[dy][dx] == 1:
                    que.append((dy, dx))
                    visit[dy][dx] = visit[ty][tx] + 1



n, m = map(int, input().split())     # n = 세로
lis = []
res = sys.maxsize

for _ in range(n):
    lis.append(list(map(int, input())))

visit = [[0 for _ in range(m)] for _ in range(n)]

bfs(0, 0, visit)
print(visit[n-1][m-1])