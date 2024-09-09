# dp로 풀기

# 규칙 = 현재 값이 이전 값보다 커야한다.
# dp[n] = k -> n번째 인덱스까지의 최대값 k

# 1 5 2 3 4 ->
# d[0] = lis[0], d[1] = if lis[1] > lis[0], max(d[0], d[1]+lis[1])
# d[2] = if 조건 성립 x이므로 d[1] 그대로
# d[3] = if lis[3] > lis[2], max(lis[0]+lis[2]+lis[3], d[2])

# 3 100 1 50

# a b c d -> if a < c < d -> sum(a c d) -> sum(a c) + l[d]
#

n = int(input())
lis = list(map(int, input().split(" ")))
dp = [0] * n

for i in range(n):
    dp[i] = lis[i]

for i in range(1, n):       # i = 3
    for j in range(i):      # j = 0 1 2
        if lis[i] > lis[j]:
            dp[i] = max(dp[i], dp[j]+lis[i])
