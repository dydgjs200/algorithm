# 길이가 n인 계단 수

# 1. 길이가 n인 수들 순회

# dp[n][m] = k -> 길이 n, 끝 자리 수 m인 계단 수 k
# dp[2] -> 10 12 21 23 32 34 ...
# dp[3] -> 101 120 121 123 210 212 232 234 321 323 343 345 ...

# m = 0 or 9 -> +1 / 1~8 -> +2
# dp[n][m] = if m == 0 or 9 = dp[n-1][m] + 1, else = dp[n-1][m]+2

n = int(input())
dp = [[0] * 10 for i in range(n+1)]

dp[0] = [0,1,1,1,1,1,1,1,1,1]

for i in range(1, n):
    dp[i][0] = dp[i-1][1]
    dp[i][9] = dp[i-1][8]

    for j in range(1,9):
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

print(sum(dp[n-1]) % 1000000000)
