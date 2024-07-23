# n은 4개 이하의 제곱수 합으로 표현 가능하다
# 제곱수의 최소 갯수

import math
import sys

n = int(input())
dp = [0] * (n+1)
maxVal = sys.maxsize

if n <= 3:
    print(n)
else:
    dp[1] = 1
    dp[2] = 2
    dp[3] = 3