# 조건 = lis[i] > lis[j] 보다 커야함

# dp[n] = n번째 인덱스에서 끝나는 가장 긴 부분수열 길이
# trace[n] = n번째 숫자가 포함된 수열에서 그 이전 숫자의 인덱스
# dp[n]이 max인 부분이 가장 긴 부분수열이고, 하나씩 줄여가며 경로를 찾을 수 있다.

n = int(input())
lis = list(map(int, input().split(" ")))
dp = [1] * n
res = []

for i in range(1, n):       # dp[i]를 채우기 위한 for문
    for j in range(i):      # i번째 인덱스 이전의 모든 인덱스를 비교
        if lis[i] > lis[j]:
            dp[i] = max(dp[j] + 1, dp[i])

print(max(dp))

maxValue = max(dp)
for i in range(n-1, -1, -1):
    if dp[i] == maxValue:
        res.append(lis[i])
        maxValue -= 1

res.reverse()
for r in res:
    print(r, end=" ")