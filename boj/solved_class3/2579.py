# 마지막은 꼭 밟아야 함 -> dp[i] 에서 lis[i]는 무조건 더해줘야함

n = int(input())
dp = [0] * 301
lis = [0] * 301

for i in range(n):
    lis[i] = int(input())

if n <= 2:
    print(sum(lis))
else:
    dp[0] = lis[0]
    dp[1] = lis[0] + lis[1]
    dp[2] = max(lis[0] + lis[1], lis[1] + lis[2])

    for i in range(3, n + 1):
        dp[i] = max(dp[i - 3] + lis[i - 1], dp[i - 2]) + lis[i]

    print(dp[-1])