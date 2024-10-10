
# 첫 인덱스는 중복이 안되게 뽑아야함 -> set(sl 배열)
# 다음부터는 입력받은 lis의 갯수에 맞게 뽑아야함..

# path -> [a,b] != [b,a]이다. 즉, 원소의 순서가 보장되어야함.

import sys

input = sys.stdin.readline

def backtracking(idx, path):
    global res
    if len(path) == m:
        if path not in res:
            res.append(path[:])
        return

    for i in range(n):
        if i != idx:
            path.append(lis[i])
            backtracking(i, path)
            path.pop()

n, m = map(int, input().split(" "))
lis = list(map(int, input().split(" ")))

lis = sorted(lis)   # 1 7 9 9
res = []

for i in range(n):
    backtracking(i, [lis[i]])

for r in res:
    print(*r)
