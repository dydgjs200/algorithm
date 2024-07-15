from collections import deque

mx = [1,-1,0,0]
my = [0, 0, -1, 1]

# visit 배열을 다 익었는지 체크함

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
                if visit[dx][dy] == -1 and lis[dx][dy] == 0:
                    que.append((dx,dy))
                    visit[dx][dy] = visit[tx][ty] + 1

    return


m, n = map(int, input().split(" "))
lis = [list(map(int, input().split(" "))) for _ in range(n)]
visit = [[-1] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if lis[i][j] == 1:
            bfs(i, j)

r = 0

for i in range(n):
    for j in range(m):
        if lis[i][j] == 0 and visit[i][j] == -1:
            r = -1
        if visit[i][j] >= r:
            r = visit[i][j]


print(r)
