from collections import deque


mx = [1,-1,0,0]
my = [0,0,-1,1]

def bfs(x,y, lis, visit):
    visit[x][y] = 1
    cnt = 1
    que = deque()
    que.append((x,y))

    while que:
        tx, ty = que.popleft()

        for i in range(4):
            dx = mx[i]+tx
            dy = my[i]+ty

            if 0 <= dx < n and 0 <= dy < n:
                if not visit[dx][dy] and lis[dx][dy] == 1:
                    visit[dx][dy] = 1
                    que.append((dx,dy))
                    cnt += 1

    return cnt


n = int(input())
lis = []

for i in range(n):
    lis.append(list(map(int, input())))


visit = [[0 for _ in range(n)] for _ in range(n)]
res = []

for i in range(n):
    for j in range(n):
        if lis[i][j] == 1 and not visit[i][j]:
            res.append(bfs(i,j,lis,visit))
res.sort()
print(len(res))
for r in res:
    print(r)