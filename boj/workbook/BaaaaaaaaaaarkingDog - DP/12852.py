n = int(input())
dp = [0] * (n + 1)
trace = [0] * (n + 1)  # 경로를 저장할 배열

if n == 1:
    print(0)
else:
    dp[1] = 0
    dp[2] = 1

    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + 1
        trace[i] = i - 1

        if i % 2 == 0 and dp[i // 2] + 1 < dp[i]:
            dp[i] = dp[i // 2] + 1
            trace[i] = i // 2  # 경로 저장

        if i % 3 == 0 and dp[i // 3] + 1 < dp[i]:
            dp[i] = dp[i // 3] + 1
            trace[i] = i // 3  # 경로 저장

    print(dp[n])

    # 경로 출력
    res = []
    while n > 0:
        res.append(n)
        n = trace[n]

    print(' '.join(map(str, res)))
