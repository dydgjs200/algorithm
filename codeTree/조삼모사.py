# 일을 아침, 저녁 두 부분으로 분리
# 일 a,b가 있을 때, 업무 강도 = pab + pba
# 아침, 저녁의 강도 차이는 최소가 되도록

# 1. 두 부분으로 나누는 조합 모두 생성 -> 백트래킹으로 아침부분 생성
# 2. 조합에서의 강도 최소값 찾기 -> ex. [1,2,3] -> 23+32 + 13+31 + 12+21

import sys

def backtracking(path):
    if len(path) == n // 2:
        combi.append(path[:])
        return

    for i in range(n):
        if path[-1] < i:
            path.append(i)
            backtracking(path)
            path.pop()

def score(group):       # [0,1], [0,4]..
    score = 0

    for i in range(len(group)):
        for j in range(i+1, len(group)):
            score += lis[group[i]][group[j]] + lis[group[j]][group[i]]

    return score


n = int(input())
lis = []
combi = []
res = sys.maxsize

for i in range(n):
    lis.append(list(map(int, input().split())))

for i in range(n):
    backtracking([i])

for afternoon in combi:
    night = [i for i in range(n) if i not in afternoon]
    res = min(res, abs(score(afternoon) - score(night)))

print(res)