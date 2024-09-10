
# dp[t][w] = k -> t 시간까지 w만큼 이동했을 때 먹을 수 있는 최대 k
# w % 2 == 0 라면, w = 0,2,4..이므로 이동하지 않은 것과 같음 -> 1번 나무임

t, w = map(int, input().split(" "))
lis = [0]

for i in range(t):
    lis.append(int(input()))

dp = [[0] * (w+1) for _ in range(t+1)]

for i in range(1, t+1):
    if lis[i] == 1:
        dp[i][0] = dp[i-1][0] + 1
    else:
        dp[i][0] = dp[i-1][0]

    for j in range(1, w+1):
        if lis[i] == 1 and j % 2 == 0:
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + 1
        elif lis[i] == 2 and j % 2 == 1:
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + 1
        else:
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j])

print(max(dp[t]))
