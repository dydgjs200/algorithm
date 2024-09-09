# 재귀호출 사용

def recursive(depth, cost, lastIdx):
    global ans
    if depth == n:
        ans = max(ans, cost)
        return
    # 이전에 선택한 값보다 큰 경우만 선택
    if lastIdx == -1 or lis[depth] > lis[lastIdx]:
        recursive(depth+1, lis[depth]+cost, depth)
    # 선택하지 않는 경우도 탐색
    recursive(depth+1, cost, lastIdx)


n = int(input())
lis = list(map(int, input().split()))
ans = 0

# 처음에 -1로 설정하여 어디서든 시작할 수 있도록
for i in range(n):
    recursive(i, 0, -1)

print(ans)
