# 세 수의 합 d가 배열에 포함될 때, 가장 큰 d 값 찾기

# 백트래킹을 통한 조합 생성 후 큰값 찾기 -> 메모리 초과
# 원소 u의 개수가 2억이므로..

def backtracking(depth, path, sum):
    global combi
    if depth == 2:
        combi.append(sum)
        return

    for i in lis:
        if path[-1] < i:
            path.append(i)
            backtracking(depth+1, path, sum+i)
            path.pop()


n = int(input())
lis = []
combi = []
res = 0

for i in range(n):
    lis.append(int(input()))


for i in range(len(lis)):
    backtracking(0, [lis[i]], lis[i])

for c in combi:
    if c in lis:
        res = max(res, c)

print(res)