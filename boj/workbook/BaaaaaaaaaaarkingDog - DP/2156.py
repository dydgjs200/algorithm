# dp[n] = k -> n번째 잔까지의 최대

# 조건 = 연속 3잔은 마실 수 없음.
# d[0] = l[0], d[1] = l[0]+l[1], d[2] = (l[0]+l[1], l[0]+l[2]),
# d[3] = (l[0]+l[1]+l[3], l[0]+l[2]+l[3])..

# 1 2 3 4 5 -> d[5] = l[5]+l[4]+d[2] or d[4]+l[5]

n = int(input())
lis = [0] * 10001

for i in range(1, n+1):
    lis[i] = int(input())

dp = [0] * 10001
dp[1] = lis[1]
dp[2] = lis[1]+lis[2]
for i in range(3, n+1):
    dp[i] = max(dp[i-3]+lis[i-1]+lis[i], dp[i-2]+lis[i], dp[i-1])

print(max(dp))