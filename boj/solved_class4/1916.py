# a -> b로 가는 버스 비용 최소화

import sys
import heapq

input = sys.stdin.readline

n = int(input())
e = int(input())
lis = [[] for _ in range(n+1)]

def dijk(node):
    dist = [sys.maxsize] * (n+1)
    dist[node] = 0
    pq = [(0, node)]

    while pq:
        current_dist, current_node = heapq.heappop(pq)

        if current_dist > dist[current_node]:
            continue

        for weight, nod in lis[current_node]:
            distance = current_dist + weight

            if distance < dist[nod]:
                dist[nod] = distance
                heapq.heappush(pq, (distance, nod))

    return dist

for _ in range(e):
    a, b, w = map(int, input().split(" "))

    lis[a].append((w, b))

start, end = map(int, input().split(" "))
ans = dijk(start)
print(ans[end])
