# dp[n] = k -> 정수 n을 1,2,3의 합으로 만드는 k 가지 방법

t = int(input())

for _ in range(t):
    n = int(input())
    dp = [0] * (n+1)

    if n <= 2:
        print(n)
    elif n == 3:
        print(4)
    else:
        dp[1] = 1
        dp[2] = 2
        dp[3] = 4
        for i in range(4, n+1):
            dp[i] = dp[i-3] + dp[i-2] + dp[i-1]

        print(dp[n])
