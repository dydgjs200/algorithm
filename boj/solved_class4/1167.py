# 트리의 지름 = 트리에서 가장 긴 경로
# 백트래킹 같은 경우 가지치기가 핵심인데, 이 문제는 모든 경로를 찾아야 하므로 부적절함.
from collections import deque

def bfs(node, weight):
    visit = [0] * (v+1)
    visit[node] = 1
    que = deque()
    que.append((node, weight))

    far_node, far_weight = 0, 0

    while que:
        top_node, top_weight = que.popleft()

        for n, w in lis[top_node]:
            if not visit[n]:
                que.append((n, top_weight + w))
                visit[n] = 1

                if top_weight + w > far_weight:
                    far_weight = top_weight + w
                    far_node = n


    return far_node, far_weight


import sys
input = sys.stdin.readline

v = int(input())
lis = [[] for _ in range(v+1)]


for _ in range(v):
    st = list(map(int, input().split(" ")))
    node, st = st[0], st[1:-1]

    for i in range(0, len(st), 2):
        lis[node].append((st[i], st[i+1]))

first_end_node, first_end_weight = bfs(1, 0)
# print(first_end_node, first_end_weight)

second_end_node, second_end_weight = bfs(first_end_node, 0)
print(second_end_weight)

