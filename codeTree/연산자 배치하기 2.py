import sys

# 백트래킹으로 연산자 조합을 만들고 처리함.

def backtracking(path):
    global op
    if len(path) == n - 1:
        op.append(path[:])
        return

    for i in range(len(oper)):
        if oper[i] > 0:
            if i == 0:
                path.append("+")
            elif i == 1:
                path.append("-")
            elif i == 2:
                path.append("*")
            oper[i] -= 1
            backtracking(path)
            oper[i] += 1
            path.pop()


n = int(input())
num = list(map(int, input().split()))
oper = list(map(int, input().split()))
op = []
maxVal, minVal = -sys.maxsize, sys.maxsize

backtracking([])

for o in op:
    res = num[0]

    for i in range(len(o)):
        if o[i] == "+":
            res += num[i + 1]
        elif o[i] == "-":
            res -= num[i + 1]
        elif o[i] == "*":
            res *= num[i + 1]

    maxVal = max(maxVal, res)
    minVal = min(minVal, res)

print(minVal, maxVal)