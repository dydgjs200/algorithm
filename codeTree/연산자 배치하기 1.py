# 정수 순서 바꾸기 불가능, + - * 세 개의 연산자
# n의 개수가 적기때문에 완전탐색으로 가능할듯.
# oper의 조합을 찾기


# 출력 = 연산의 최소 최대값

# 1. 연산자의 횟수만큼 연산자 배열을 만들어주기 -> ex. 1 1 0 -> [+-]
# 2. 연산자 배열을 백트래킹으로 조합 만들기 -> [+-], [-+]
# 3. 모든 조합에 대해 max, min 값 계산하기

from itertools import permutations
import sys

n = int(input())
num = list(map(int, input().split()))
oper = list(map(int, input().split()))      # 연산자는 덧셈 뺄셈 곱셈 순
op = []
maxVal, minVal = -sys.maxsize, sys.maxsize

for i in range(len(oper)):
    for j in range(oper[i]):
        if i == 0:
            op.append("+")
        elif i == 1:
            op.append("-")
        elif i == 2:
            op.append("*")

com = permutations(op, n-1)

for c in com:
    res = num[0]

    for i in range(len(c)):
        if c[i] == "+":
            res += num[i+1]
        elif c[i] == "-":
            res -= num[i+1]
        if c[i] == "*":
            res *= num[i+1]

    maxVal = max(maxVal, res)
    minVal = min(minVal, res)

print(minVal, maxVal)