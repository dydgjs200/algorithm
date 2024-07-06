from collections import deque

def bfs(node):
    que = deque()
    que.append(node)
    visit[node] = 1

    while que:
        top = que.popleft()

        for i in lis[top]:
            if not visit[i]:
                visit[i] = 1
                que.append(i)

n = int(input())
m = int(input())
lis = [[] for _ in range(n+1)]
visit = [0 for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split(" "))
    lis[a].append(b)
    lis[b].append(a)

bfs(1)
print(sum(visit)-1)