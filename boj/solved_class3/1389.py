# 양방향 그래프
# 거리 값은 이전 값에 대한 + 1 -> visit[n] = visit[n-1]+1

from collections import deque

def bfs(node):
    que = deque()
    que.append(node)
    visit[node] = 0

    while que:
        top = que.popleft()

        for i in range(1, n+1):
            if lis[i][top] == 1 and visit[i] == -1:
                visit[i] = visit[top] + 1
                que.append(i)



n, m = map(int, input().split(" "))
lis = [[0 for _ in range(n+1)] for _ in range(n+1)]
res = []

for _ in range(m):
    a, b = map(int, input().split(" "))
    lis[a][b] = lis[b][a] = 1

for i in range(1, n+1):
    visit = [-1 for _ in range(n+1)]
    bfs(i)
    res.append(sum(visit))


print(res.index(min(res))+1)