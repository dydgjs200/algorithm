# 재귀나 dp으로 일이 겹치지 않는 최대 수익

def recursive(depth, cost):
    global res

    if depth > n:
        return
    elif depth == n:
        res = max(res, cost)
        return

    recursive(depth+lis[depth][0], cost+lis[depth][1])
    recursive(depth+1, cost)


n = int(input())
lis = []
res = 0

for i in range(n):
    t, p = map(int, input().split())
    lis.append((t,p))

recursive(0, 0)
print(res)