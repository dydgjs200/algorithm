# dp[n] = k -> 숫자 n을 1,2,3 더하기로 나타내는 총 가짓 수 k

test = int(input())

for i in range(test):
    n = int(input())
    dp = [0] * (n + 1)
    dp[1] = 1       # 1 = 1
    dp[2] = 2       # 2 = 1+1, 2
    dp[3] = 4        # 3 = 1+1+1, 2+1, 1+2, 3

    if n <= 3:
        print(dp[n])
        continue
    else:
        for i in range(4, n+1):
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

        print(dp[n])
