# n*n 정사각형 , m 개의 바이러스 (상하좌우)
# 0 = 빈칸, 1 = 벽, 2 = 바이러스
import copy
# 즉, m개의 바이러스를 2번 칸 중 선택해서 넣고, 모든 빈칸에 퍼뜨리는 최소시간
# 1. 바이러스 후보지역을 리스트로 만듦 -> 백트래킹
# 2. 1번의 리스트 중 m 개를 뽑는 조합을 모두 생성
# 3. 조합에 대해 bfs를 통해 퍼뜨리는 시간을 계산
# 3.3 맵의 빈칸 체크 함수로 계속 체크

import sys
from collections import deque

mx = [1,-1,0,0]
my = [0,0,-1,1]

def checkVirus(arr):       # 바이러스가 퍼진 지도에 모든 칸이 바이러스인지 체크
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 0:
                return False

    return True

def backtracking(path, visit, startIdx):     # path = 바이러스 후보지 중 m 개의 조합 인덱스
    global virusCombi

    if len(path) == m:
        virusCombi.append(path[:])
        return

    for i in range(startIdx+1, len(virusArea)):
        if not visit[i]:
            visit[i] = 1
            path.append(i)
            backtracking(path, visit, i)
            visit[i] = 0
            path.pop()

def bfs(arr, arrVisit, que):
    global res
    cnt = 0

    while que:
        tx, ty = que.popleft()

        for i in range(4):
            dx = mx[i] + tx
            dy = my[i] + ty

            if 0 <= dx < n and 0 <= dy < n:
                if arrVisit[dx][dy] == 0 and arr[dx][dy] == 0:
                    arrVisit[dx][dy] = arrVisit[tx][ty] + 1
                    que.append((dx, dy))
                    arr[dx][dy] = 2
                    cnt = max(cnt, arrVisit[dx][dy])

    return cnt

# input = sys.stdin.input

n, m = map(int, input().split(" "))
lis = []
virusArea = []
virusCombi = []
res = sys.maxsize     # 정답

for i in range(n):
    l = list(map(int, input().split(" ")))
    lis.append(l)

    for j in range(len(l)):
        if l[j] == 2:
            virusArea.append((i,j))

visit = [0 for _ in range(len(virusArea))]

for i in range(n):
    backtracking(path=[i], visit=visit, startIdx=i)

print(virusArea)
print(virusCombi)

for v in virusCombi:        # virusArea idx -> [0,1,3]  ->
    arr = copy.deepcopy(lis)
    que = deque()
    arrVisit = [[0 for _ in range(n)] for _ in range(n)]

    for idx in v:
        x, y = virusArea[idx][0], virusArea[idx][1]
        que.append((x,y))       # que에는 바이러스의 위치가 들어가 있어야함.
        arrVisit[x][y] = 1         # 초기 바이러스 위치는 방문처리
        arr[x][y] = 2

    c = bfs(arr, arrVisit, que)


    if checkVirus(arr):
        res = min(res, c-1)

if res != sys.maxsize:
    print(res)
else:
    print(-1)


