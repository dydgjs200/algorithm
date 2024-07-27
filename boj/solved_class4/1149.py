# 이전 집과 다른 색 -> 이전 항의 열과 같으면 안된다는 것.
import sys

n = int(input())
dp = [[0] * 3 for _ in range(n+1)]
r = 0

for i in range(1, n+1):
    a, b, c = map(int, input().split(" "))

    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + a
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + b
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + c

    r = min(dp[i][0], dp[i][1], dp[i][2])

print(r)