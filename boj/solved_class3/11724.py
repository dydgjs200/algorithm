from collections import deque
import sys

def bfs(node):
    que = deque()
    que.append(node)
    visit[node] = 1

    while que:
        top = que.popleft()

        for i in range(1, n+1):
            if not visit[i] and lis[top][i] == 1:
                que.append(i)
                visit[i] = 1

    return

input = sys.stdin.readline

n, m = map(int, input().split(" "))
lis = [[0] * (n+1) for _ in range(n+1)]
visit = [0] * (n+1)
cnt = 0


for _ in range(m):
    a, b = map(int, input().split(" "))
    lis[a][b] = lis[b][a] = 1

for i in range(1, n+1):
    if not visit[i]:
        bfs(i)
        cnt += 1

print(cnt)