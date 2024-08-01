# 노드 n, 도로 m(양방), 웜홀 w(단방향)
# 웜홀 사용 시 시간이 뒤로 감
# n에서 사이클 형성 시 원래 시간보다 뒤로 가 있는지?

# 음의 사이클에 대한 문제 -> 벨만포드
# 간선을 모두 최단거리 체크한 뒤, 한번 더 체크할 경우 음의 사이클을 찾을 수 있다.

import sys
input = sys.stdin.readline

def bellman(start, n, edge):
    dist = [sys.maxsize] * (n+1)
    dist[start] = 0

    # 각 노드마다 전체를 검색
    for i in range(n):
        for u,v,w in edge:
            if dist[u] != sys.maxsize and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

                if i == n-1:
                    return True

    return False

tc = int(input())

for _ in range(tc):
    n, m, w = map(int, input().split())
    edges = []
    res = False

    # 도로 정보 입력
    for _ in range(m):
        u, v, c = map(int, input().split())
        edges.append((u, v, c))
        edges.append((v, u, c))

    # 웜홀 정보 입력
    for _ in range(w):
        u, v, c = map(int, input().split())
        edges.append((u, v, -c))        # 웜홀은 시간이 음수이므로 -c

    for i in range(1, n+1):
        if bellman(i, n, edges):
            res = True
            break
    if res:
        print("YES")
    else:
        print("NO")