# 뽑는 시간이 주어질 때 모든 사람이 돈을 출력하는데 걸리는 최소 시간
# 출력은 누적 합임. 즉, 총 3명 있다면 -> i0+(i0+i1)+(i0+i1+i2)
# lis(idx, cost) 일 때 cost로 정렬

from itertools import combinations

n = int(input())
num = list(map(int, input().split(" ")))
res = 0

num = sorted(num)

for i in range(1, n+1):
    res += sum(num[:i])

print(res)


