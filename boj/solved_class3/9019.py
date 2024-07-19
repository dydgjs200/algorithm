# a,b가 주어질 때 b를 통해 어떠한 연산이 이뤄졌는가?
# 예시처럼 3412를 4가지 연산으로 백트래킹?

from collections import deque

def bfs(node, path, end):
    que = deque()
    que.append((node, ""))

    while que:
        top_node, top_oper = que.popleft()

        if top_node == end:      # 목표를 찾았다면
            print(top_oper)
            return

        str_node = str(top_node)

        #D
        d = (top_node*2) % 10000
        if d not in path:
            path.append(d)
            que.append((d, top_oper + "D"))

        #S
        s = (top_node-1) % 10000
        if s not in path:
            path.append(s)
            que.append((s, top_oper + "S"))



t = int(input())

for _ in range(t):
    a, b = map(int, input().split(" "))

    print(bfs(b, [], a))
