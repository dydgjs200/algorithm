# dp[i] = k -> i일까지의 최대 k값

# 조건 = t[i] + i <= n (상담 총 수가 n을 넘지 말아야한다.)

n = int(input())
dp = [0] * (n+1)
t, p = [], []

for i in range(n):
    a, b = map(int, input().split(" "))

    t.append(a)
    p.append(b)

val = 0

for i in range(n-1, -1, -1):
    if t[i] + i <= n:
        dp[i] = max(dp[i+t[i]] + p[i], val)
        val = dp[i]
    else:
        dp[i] = val

print(val)