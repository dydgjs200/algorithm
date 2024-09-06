# 1 or 2계단씩, 연속된 3계단은 밟지 못함
# dp[n] = k -> n번째 계단까지의 최대값 k
# dp[n] = max(dp[i-2] + lis[i], dp[i-1])
# 마지막 도착계단은 반드시 밟아야함.

# 연속된 세 계단이 안된다는 것은 dp[i] = max(lis[i-1] + dp[i-3] + lis[i], dp[i-2] + lis[i])

n = int(input())
lis = [0]

for i in range(n):
    lis.append(int(input()))

dp = [0] * (n+1)

if n == 1:
    print(lis[1])
else:
    dp[1] = lis[1]
    dp[2] = lis[1]+lis[2]

    for i in range(3, n+1):
        dp[i] = max(dp[i-2], dp[i-3]+lis[i-1]) + lis[i]

    print(dp[n])
