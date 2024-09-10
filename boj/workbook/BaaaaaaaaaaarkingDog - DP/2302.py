# n번까지 있으며 좌석은 왼, 오른쪽 이동 가능
# ex. 7번 = 6 7 8에 앉을 수 있음
# vip는 옆으로 못 옮김.

# vip 좌석이 주어질 때 사람들이 좌석에 앉는 방법 수
# 가짓 수 제한이 매우 크기에 dp 쪽으로..

# dp[n] = k -> n번째 좌석까지의 만들 수 있는 가짓 수 k
# d[1] = 1, d[2] = 12 21, d[3] = 123, 213, 132, d[4] = 1234, 2134, 2143, 1324, 1243

# vip를 기준으로 두 부분을 분할(고정되어 있기 때문)
# ex. 좌석 10개에 3, 7이 vip면 -> 1~2, 4~6, 8~10 세부분으로 분할
# 분할 된 영역은 독립적이기에 곱 연산임
# 즉, 세 부분은 좌석 수에 따라 fibo(2), fibo(3), fibo(3)이므로 이것을 다 곱한 값

n = int(input())    # 좌석 수
m = int(input())    # vip 수
lis = [int(input()) for _ in range(m)]      # vip 리스트
res = 1
dp = [0] * (n+1)
dp[1] = 1
dp[2] = 2

for i in range(3, n+1):
    dp[i] = dp[i-1] + dp[i-2]

lastIdx = 0

for vip in lis:
    res *= dp[vip - lastIdx - 1]
    lastIdx = vip

res *= dp[n - lastIdx]
print(res)

