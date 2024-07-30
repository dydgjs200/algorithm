import heapq
import sys

input = sys.stdin.readline

def dijk(node):
    dist = [sys.maxsize] * (v+1)
    dist[node] = 0
    pq = [(0, node)]

    while pq:
        current_dist, current_node = heapq.heappop(pq)

        if current_dist > dist[current_node]:
            continue

        for n, w in lis[current_node]:
            dist_cal = w + current_dist

            if dist_cal < dist[n]:
                dist[n] = dist_cal
                heapq.heappush(pq, (dist_cal, n))

    return dist

v, e = map(int, input().split(" "))
start = int(input())
lis = [[] for _ in range(v+1)]

for _ in range(e):
    a, b, w = map(int, input().split(" "))
    lis[a].append((b, w))

dist = dijk(start)
dist[0] = 0

dist = dist[1:]
for i in dist:
    if i != sys.maxsize:
        print(i)
    else:
        print("INF")
