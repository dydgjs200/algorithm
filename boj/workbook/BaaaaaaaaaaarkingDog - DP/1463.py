# 재귀적 요소 파악
# 수식 세우기
# 초기값 설정

# dp[n] = k -> 숫자 n에 대한 k번의 연산
# n = 10 -> 10 9 3 1 / 10 5 4 2 1 ..

n = int(input())
dp = [0] * (n+1)
dp[1] = 0

for i in range(2, n+1):
    dp[i] = dp[i-1] + 1

    if i % 2 == 0:
        dp[i] = min(dp[i//2] + 1, dp[i])
    if i % 3 == 0:
        dp[i] = min(dp[i//3] + 1, dp[i])

print(dp[n])