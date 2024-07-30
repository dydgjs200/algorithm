# 단방향 그래프, 사이클 형성 후 다시 돌아올 때 걸리는 학생들의 최대 시간
# 하지만, 노드에서 노드로 가는 길은 최단거리만을 택해야함 -> 다익스트라

# 최단 거리부터 갱신하기 위해 heapq를 사용함
# 거리부터 정렬하기 위해서 (가중치, 노드)로 저장해야함.
import heapq
import sys
input = sys.stdin.readline

def dijk(node, n):
    dist = [sys.maxsize] * (n+1)
    dist[node] = 0
    pq = []
    pq.append((0, node))

    while pq:
        current_dist, current_node = heapq.heappop(pq)

        if dist[current_node] < current_dist:
            continue

        for n, w in lis[current_node]:
            dist_cal = w + current_dist

            if dist_cal < dist[n]:
                dist[n] = dist_cal
                heapq.heappush(pq, (dist_cal, n))

    return dist

n, m, x = map(int, input().split(" "))
lis = [[] for _ in range(n+1)]
visit = [0] * (n+1)

for _ in range(m):
    a, b, w = map(int, input().split(" "))

    lis[a].append((b,w))

ans = dijk(x, n)        # x 노드에서 각 노드까지의 최단거리
ans[0] = 0
for i in range(1, n+1):
    if i != x:
        res = dijk(i, n)        # x를 제외한 모든 노드에서 최단 거리를 더해줘야함.
        ans[i] += res[x]

print(max(ans))