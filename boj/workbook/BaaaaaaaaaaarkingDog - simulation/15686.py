# 0 = 빈칸, 1 = 집, 2 = 치킨집
# 치킨 거리 = 집과 가장 가까운 치킨집 거리
# 출력 = 집과 가장 가까운 치킨집 거리가 최소가 되는 값

# r = y축, c = x축 ( r,c >= 1)

# 문제 = 각 집에서 치킨 거리가 최소가 되도록 m개만을 남기고 없애야함.
# 1. 치킨집 좌표 중 백트래킹을 통해 m개만 남기는 모든 경우의 수 -> 인덱스를 구함
# 2. 구한 인덱스를 바탕으로 m개의 위치 파악
# 3. 해당 위치에서 집을 하나씩 가져오며 거리 총 합 구하기

import sys

def backtracking(path):
    global chicken_combi

    if len(path) == m:
        chicken_combi.append(path[:])
        return

    for i in range(len(chicken_area)):
        if path[-1] < i:
            path.append(i)
            backtracking(path)
            path.pop()

n, m = map(int, input().split(" "))
lis = []
chicken_area = []       # 치킨집 좌표
chicken_combi = []      # 치킨집 조합 -> 좌표에 대한 인덱스 값으로 구성
house = []
res = sys.maxsize

for _ in range(5):
    lis.append(list(map(int, input().split(" "))))

for r in range(5):
    for c in range(5):
        if lis[r][c] == 1:
            house.append((r,c))
        if lis[r][c] == 2:
            chicken_area.append((r,c))


# 치킨집의 인덱스를 조합으로 생성
for i in range(len(chicken_area)):
    backtracking([i])

for combi in chicken_combi:     # combi = [0,1] -> 0,1번의 치킨집 인덱스
    total_dist = 0
    for h in house:  # 모든 집에 대해 가장 가까운 치킨집과의 거리 계산
        hr, hc = h[0], h[1]
        min_dist = sys.maxsize  # 집마다 최소 치킨 거리를 계산
        for c in combi:
            cr, cc = chicken_area[c][0], chicken_area[c][1]
            min_dist = min(min_dist, abs(cr - hr) + abs(cc - hc))
        total_dist += min_dist

        # 최소 치킨 거리를 업데이트
    res = min(res, total_dist)

print(res)



