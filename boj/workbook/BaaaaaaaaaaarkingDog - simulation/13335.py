# que.append 시점은 que의 합 + 현재 트럭 <= l 일때
# que.pop 시점은 else일 때

from collections import deque

n, w, l = map(int, input().split(" "))  # w = 다리 길이, l = 최대 하중
truck = list(map(int, input().split(" ")))
res = 0

que = deque([0] * w)
weight = 0

for t in truck:
    while True:
        res += 1
        weight -= que.popleft()

        if weight + t <= l:
            que.append(t)
            weight += t
            break
        else:
            que.append(0)

res += w

print(res)


