from collections import deque

mx = [1, -1, 0, 0]
my = [0, 0, -1, 1]

def bfs(y, x, visit):
    global maxWidth
    count = 1       # 현재 위치도 그림임

    que = deque()
    que.append((y, x))
    visit[y][x] = 1

    while que:
        ty, tx = que.popleft()

        for i in range(4):
            dy = my[i] + ty
            dx = mx[i] + tx

            if 0 <= dy < n and 0 <= dx < m:
                if not visit[dy][dx] and lis[dy][dx] == 1:
                    visit[dy][dx] = 1
                    count += 1
                    que.append((dy, dx))

    maxWidth = max(maxWidth, count)

    return

n, m = map(int, input().split(" "))     # n = 세로
lis = []
picture = 0
maxWidth = 0

for _ in range(n):
    lis.append(list(map(int, input().split(" "))))

visit = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n):
    for j in range(m):
        if not visit[i][j] and lis[i][j] == 1:
            bfs(i, j, visit)
            picture += 1


print(picture)
print(maxWidth)