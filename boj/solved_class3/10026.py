# RGB 영역에서 적록색약은 RG가 같게 보임
# 출력 = 아닌사람, 맞는사람 순으로의 영역 -> BFS

from collections import deque

mx = [1,-1,0,0]
my = [0,0,-1,1]

def bfs(x,y,type, arr):
    que = deque()
    que.append((x,y))
    visit[x][y] = 1

    while que:
        tx, ty = que.popleft()

        for i in range(4):
            dx = mx[i] + tx
            dy = my[i] + ty

            if 0 <= dx < n and 0 <= dy < n:
                if not visit[dx][dy] and arr[dx][dy] == type:
                    que.append((dx,dy))
                    visit[dx][dy] = 1

    return


n = int(input())
lis = []
res1, res2 = 0, 0

for _ in range(n):
    lis.append(list(map(str, input())))

arr = [[0] * n for _ in range(n)]
visit = [[0] * n for _ in range(n)]

# 적록색약일 경우 RG = 1로 표현

for i in range(n):
    for j in range(n):
        if lis[i][j] == "R" or lis[i][j] == "G":
            arr[i][j] = 1
        else:
            arr[i][j] = 0

for i in range(n):
    for j in range(n):
        if not visit[i][j]:
            res1 += 1
            bfs(i,j,type=arr[i][j], arr=arr)

arr = [[0] * n for _ in range(n)]
visit = [[0] * n for _ in range(n)]

# 아닐 경우 R = 0, G = 1, B = 2로 표현
for i in range(n):
    for j in range(n):
        if lis[i][j] == "R":
            arr[i][j] = 0
        elif lis[i][j] == "G":
            arr[i][j] = 1
        else:
            arr[i][j] = 2

for i in range(n):
    for j in range(n):
        if not visit[i][j]:
            res2 += 1
            bfs(i,j,type=arr[i][j], arr=arr)

print(res2, res1)

