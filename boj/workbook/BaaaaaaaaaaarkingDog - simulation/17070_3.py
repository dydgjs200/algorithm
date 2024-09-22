# dp
# d[y][x][pipe] = y,x에서의 pipe일 때 경우의 수

n = int(input())
lis = []
dp = [[[0] * 3 for _ in range(n)] for _ in range(n)]

for _ in range(n):
    lis.append(list(map(int, input().split(" "))))

dp[0][1][0] = 1     # 초기 가로 파이프

for r in range(n):
    for c in range(2, n):
        if lis[r][c] == 1:
            continue

        if c-1 >= 0 and lis[r][c-1] == 0:
            dp[r][c][0] = dp[r][c-1][0] + dp[r][c-1][2]

        if r-1 >= 0 and lis[r-1][c] == 0:
            dp[r][c][1] = dp[r-1][c][1] + dp[r-1][c][2]

        if r-1 >= 0 and c-1 >= 0 and lis[r-1][c-1] == 0 and lis[r-1][c] == 0 and lis[r][c-1] == 0:
            dp[r][c][2] = dp[r-1][c-1][1] + dp[r-1][c-1][0] + dp[r-1][c-1][2]

print(dp[n-1][n-1][2] + dp[n-1][n-1][1] + dp[n-1][n-1][0])