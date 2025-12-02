from collections import deque


my = [0, 0, -1, 1]
mx = [1, -1, 0, 0]

def bfs(y,x):
    lis[y][x] = 0
    que = deque()
    que.append((y,x))

    while que:
        ty, tx = que.popleft()

        for i in range(4):
            dy = ty + my[i]
            dx = tx + mx[i]

            if 0 <= dy < n and 0 <= dx < m:
                if lis[dy][dx] == 1:
                    lis[dy][dx] = 0
                    que.append((dy, dx))

t = int(input())

for _ in range(t):
    m, n, k = map(int, input().split(" "))      # 가로 m, 세로 n, 배추개수 k
    lis = [[0 for _ in range(m)] for _ in range(n)]
    cnt = 0

    for b in range(k):
        x, y = map(int, input().split(" "))
        lis[y][x] = 1

    for y in range(n):
        for x in range(m):
            if lis[y][x] == 1:
                bfs(y,x)
                cnt += 1

    print(cnt)
