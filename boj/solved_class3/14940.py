# 못 가는 곳을 -1로 처리해야함

from collections import deque

mx = [1, -1, 0, 0]
my = [0, 0, -1, 1]

def bfs(x, y):
    visit[x][y] = 0
    que = deque()
    que.append((x,y))

    while que:
        tx, ty = que.popleft()

        for i in range(4):
            dx = mx[i] + tx
            dy = my[i] + ty

            if 0 <= dx < n and 0 <= dy < m:
                if visit[dx][dy] == -1 and lis[dx][dy] == 1:
                    que.append((dx, dy))
                    visit[dx][dy] = visit[tx][ty] + 1

    return


n, m = map(int, input().split(" "))
lis = []
visit = [[-1] * m for _ in range(n)]

for _ in range(n):
    lis.append(list(map(int, input().split(" "))))

for i in range(n):
    for j in range(m):
        if lis[i][j] == 2:
            bfs(i, j)



for i in range(n):
    for j in range(m):
        if lis[i][j] == 0:
            print(0, end=" ")
        else:
            print(visit[i][j], end=" ")
    print()
