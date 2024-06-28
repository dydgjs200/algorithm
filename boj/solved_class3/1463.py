# 숫자를 3가지 방법으로 연산했을 때 1로 만들어지는 최단거리
# 1. 재귀 처리 -> 시간 초과
# import sys
#
# def dfs(num, cnt):
#     global res
#     if num == 1:
#         res = min(res, cnt)
#         return
#     if num % 2 == 0:
#         dfs(num//2, cnt+1)
#     if num % 3 == 0:
#         dfs(num//3, cnt+1)
#     dfs(num-1, cnt + 1)
#
# n = int(input())
# res = sys.maxsize
#
# dfs(n, 0)
# print(res)

# 2. dp로 풀기
n = int(input())
dp = [0] * (n+1)

for i in range(2, n+1):
    dp[i] = dp[i-1] + 1
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)

print(dp[n])