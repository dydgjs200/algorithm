# 양방향, 1번에서 n번으로 가는 최단거리
# 주어진 임의의 정점은 반드시 통과해야함
# 한번 이동했던 간선도 다시 이동 가능

# 주어진 임의의 정점을 지나야한다 -> 임의의 정점에서 n까지의 최단경로?
# 즉, 1에서 임의 정점까지의 최단 경로 에서 n까지의 최단 경로를 찾자
# 임의의 정점은 두 개가 고정적으로 주어짐.

import heapq
import sys
input = sys.stdin.readline

def dijk(node):
    dist = [sys.maxsize] * (n+1)
    dist[node] = 0
    pq = [(0, node)]        # 가중치, 노드 순

    while pq:
        current_dist, current_node = heapq.heappop(pq)

        if current_dist > dist[current_node]:  # end보다 n이 크면 종료
            continue

        for weight, no in lis[current_node]:
            distance = current_dist + weight

            dist[no] = min(dist[no], distance)
            heapq.heappush(pq, (distance, no))

    return dist

n, e = map(int, input().split(" "))
lis = [[] for _ in range(n+1)]

for _ in range(e):
    a, b, w = map(int, input().split(" "))
    lis[a].append((w, b))  # 가중치, 노드
    lis[b].append((w, a))        # 양방향

v1, v2 = map(int, input().split(" "))
dist_1 = dijk(1)        # 1에서 n까지의 최단경로 -> dist_1[v1] = 1에서 v1까지의 경로 값
dist_v1 = dijk(v1)
dist_v2 = dijk(v2)

# case1 = 1 -> v1 -> v2 -> n
route1 = dist_1[v1] + dist_v1[v2] + dist_v2[n]

# case2 = 1 -> v2 -> v1 -> n
route2 = dist_1[v2] + dist_v2[v1] + dist_v1[n]

result = min(route1, route2)

if result >= sys.maxsize:
    print(-1)
else:
    print(result)
