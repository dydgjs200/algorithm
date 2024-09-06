n = int(input())
dp = [[0]*3 for _ in range(n)]
lis = []

for i in range(n):
    lis.append(list(map(int, input().split())))

# 첫 번째 집의 비용은 선택한 색 그대로 저장
dp[0][0] = lis[0][0]  # 첫 집을 빨간색으로 칠한 비용
dp[0][1] = lis[0][1]  # 첫 집을 초록색으로 칠한 비용
dp[0][2] = lis[0][2]  # 첫 집을 파란색으로 칠한 비용

# DP 테이블 채우기
for i in range(1, n):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + lis[i][0]  # 빨강을 선택한 경우
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + lis[i][1]  # 초록을 선택한 경우
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + lis[i][2]  # 파랑을 선택한 경우

# 마지막 집에서 세 색 중 최소 비용을 선택
result = min(dp[n-1][0], dp[n-1][1], dp[n-1][2])
print(result)
