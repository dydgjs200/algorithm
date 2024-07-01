import sys
from collections import deque

def bfs(node):
    que = deque()
    cnt = 0
    que.append((node, cnt))

    while que:
        top, cnt = que.popleft()
        visit[top] = 1

        if top == m:
            print(cnt)
            break
        for i in [top-1, top+1, top*2]:
            if 0 <= i < maxSize and not visit[i]:
                que.append((i, cnt+1))


n, m = map(int, input().split(" "))
maxSize = 100001
visit = [0 for _ in range(maxSize)]

bfs(n)