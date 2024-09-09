
# dp[t][w] = k -> t 시간까지 w만큼 이동했을 때 먹을 수 있는 최대 k


t, w = map(int, input().split(" "))
lis = [0]

for i in range(t):
    lis.append(int(input()))

dp = [[0] * (w+1) for _ in range(t+1)]

