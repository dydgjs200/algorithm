# 세로 n , 가로 m
# 벽은 꼭 3개를 세워야함

# 안전 영역의 최대

# 1. 백트래킹을 통한 벽 3개 세우기 -> 벽 좌표를 3개 고르는걸로..
# 2. bfs를 통한 바이러스 퍼뜨리기
# 3. 안전 영역 크기 구하기

import copy
from collections import deque
import sys

mx = [1, -1, 0, 0]
my = [0, 0, -1, 1]

input = sys.stdin.readline

def backtracking(startIdx, path):
    global createWall

    if len(path) == 3:
        createWall.append(path[:])
        return

    for i in range(startIdx+1, len(wall)):
        path.append(i)
        backtracking(i, path)
        path.pop()

def bfs(arr, visit, que):
    while que:
        ty, tx = que.popleft()

        for i in range(4):
            dy = my[i] + ty
            dx = mx[i] + tx

            if 0 <= dy < n and 0 <= dx < m:
                if arr[dy][dx] == 0 and not visit[dy][dx]:
                    visit[dy][dx] = 1
                    que.append((dy, dx))
                    arr[dy][dx] = 2
    return

def checkSafeArea(arr):
    cnt = 0

    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                cnt += 1

    return cnt

n, m = map(int, input().split(" "))
lis = []
createWall = []     # wall 인덱스를 3개 선택하는 경우의 수
wall = []       # 입력받은 벽 좌표
virus = []      # 바이러스 좌표
res = 0         # 안전영역 최대크기

for i in range(n):
    l = list(map(int, input().split(" ")))
    lis.append(l)

    for j in range(len(l)):
        if l[j] == 0:
            wall.append((i, j))

        elif l[j] == 2:
            virus.append((i, j))


for i in range(len(wall)):
    backtracking(i, [i])


for idx in createWall:
    arr = copy.deepcopy(lis)
    que = deque()
    visit = [[0 for _ in range(m)] for _ in range(n)]

    for i in idx:
        wy, wx = wall[i][0], wall[i][1]     # 선택된 벽의 좌표

        arr[wy][wx] = 1     # copy한 배열에 벽 세우기

    # que에 바이러스 위치 넣기
    for i in virus:
        que.append((i[0], i[1]))
        visit[i[0]][i[1]] = 1       # 초기 바이러스 위치 체크

    bfs(arr, visit, que)
    res = max(res, checkSafeArea(arr))

print(res)


