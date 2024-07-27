from collections import deque

mx = [1, -1, 0, 0]
my = [0, 0, -1, 1]

def bfs(x, y):
    global cnt
    visit[x][y] = 1
    que = deque()
    que.append((x,y))

    while que:
        tx, ty = que.popleft()

        for i in range(4):
            dx = mx[i] + tx
            dy = my[i] + ty

            if 0 <= dx < n and 0 <= dy < m:
                if not visit[dx][dy]:
                    if lis[dx][dy] == "X":
                        continue
                    else:
                        que.append((dx,dy))
                        visit[dx][dy] = 1

                        if lis[dx][dy] == "P":
                            cnt += 1


n, m = map(int, input().split(" "))
lis = []
cnt = 0
visit = [[0] * m for _ in range(n)]

for _ in range(n):
    st = list(map(str, input()))
    lis.append(st)

for i in range(n):
    for j in range(m):
        if lis[i][j] == "I":
            bfs(i, j)
            break

if cnt >= 1:
    print(cnt)
else:
    print("TT")

