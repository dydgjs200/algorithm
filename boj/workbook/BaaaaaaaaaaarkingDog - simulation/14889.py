# n = 짝수
# 능력치 -> Sij + Sji 이며, 두 팀의 능력치 차이를 최소로
# 두 팀으로 나눠야하기 때문에 n을 절반으로 줄여야함.

# n <= 20이므로 완전탐색도 가능할듯
# 백트래킹으로 n을 두부분의 조합으로 나누기?

import sys

def backtracking(path):
    global team

    if len(path) == n//2:
        team.append(path[:])
        return

    for i in range(1, n):
        if i > path[-1]:
            path.append(i)
            backtracking(path)
            path.pop()

def score(t):
    num = 0
    for i in range(len(t)):
        for j in range(i+1, len(t)):
            num += lis[t[i]][t[j]] + lis[t[j]][t[i]]

    return num

n = int(input())
lis = []
team = []
res = sys.maxsize

for i in range(n):
    lis.append(list(map(int, input().split(" "))))

backtracking([0])

for t in team:
    team2 = [i for i in range(n) if i not in t]

    sc = abs(score(t) - score(team2))
    res = min(res, sc)

print(res)
