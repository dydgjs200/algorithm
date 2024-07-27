# 진실을 아는 사람이 없는 파티의 개수 최대값 -> 즉 진실 0이면 파티 개수만큼임
# 즉, 진실을 아는 사람이 있으면 그 파티는 안되는거?
# 또 다른 파티에서 들었어도 안된다. -> 즉, 진실 아는 사람이 포함된 파티의 모든 원소는 진실을 알게된다.

# union-find로 가능?
# party 원소를 하나씩 가져와서 연결 시킬 때, find 과정에서 know 배열 안의 원소와
# 연결이 되어있다면 그 파티는 cnt가 추가되지않는다.

# 즉, 해당 노드를 추가할 때, find로 부모를 탐색 후 아는 사람이 없다면 union

import sys
input = sys.stdin.readline

n, m = map(int, input().split(" "))     # n = 인원, m = 파티 수
know = set(input().split()[1:])
party = []
cnt = 0

for _ in range(m):
    party.append(set(input().split()[1:]))

for _ in range(m):
    for p in party:
        if p & know:
            know = know.union(p)

for p in party:
    if p & know:
        continue
    cnt += 1

print(cnt)