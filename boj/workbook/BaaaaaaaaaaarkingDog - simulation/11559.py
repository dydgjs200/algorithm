# 같은 색이 4개 이상 상하좌유 연결 시 터짐 -> 테트리스처럼 위에 있던 애들이 내려옴
# 상대방의 필드가 주어질 때 연쇄가 몇번일지?

# 1. 주어진 맵에서 연쇄를 찾음
# 2. 연쇄를 제거하고, 위의 칸을 아래로 이동 (턴을 생각해야할듯..)

# bfs로 연쇄들을 찾고 제거 -> 한칸씩 아래로 당김 -> 이걸 반복.
# bfs를 각 좌표에서 charType을 하나씩 해줘야할듯..

mx = [1, -1, 0, 0]
my = [0, 0, -1, 1]

from collections import deque
import copy

def bfs(charType, arr, visit, y, x):
    que = deque()
    que.append((y,x))
    visit[y][x] = 1
    cnt = 1         # 연쇄 개수는 4개 이상!

    path = [(y, x)]       # 지금까지 온 좌표 경로

    while que:
        ty, tx = que.popleft()

        for i in range(4):
            dx = mx[i] + tx
            dy = my[i] + ty

            if 0 <= dy < 12 and 0 <= dx < 6:
                if not visit[dy][dx] and arr[dy][dx] == charType:
                    visit[dy][dx] = 1
                    que.append((dy, dx))
                    cnt += 1
                    path.append((dy, dx))

    if cnt < 4:     # 연쇄가 4개 미만
        return False        # 연쇄가 발생하지 않을 경우 False
    else:
        for p in path:
            py, px = p[0], p[1]

            arr[py][px] = "."  # 4연쇄가 발동한 좌표
        return True

# 연쇄가 발생한 좌표를 빈칸으로 복구해야함.
def changeChained(arr):
    for col in range(6):
        stack = []
        for row in range(11, -1, -1):
            if arr[row][col] != ".":
                stack.append(arr[row][col])

        for row in range(11, -1, -1):
            arr[row][col] = stack.pop() if stack else "."


lis = []
charType = ["R", "G", "B", "P", "Y"]        # 글자 타입
res = 0

for _ in range(12):
    l = list(map(str, input()))
    lis.append(l)

while True:        # 연쇄가 없다면 종료
    chainCount = 0      # 연쇄의 개수
    flag = True         # bfs로 4연쇄를 찾았는지 여부

    visit = [[0 for _ in range(6)] for _ in range(12)]      # 연쇄 후 당기기 함수 다음 초기화
    arr = copy.deepcopy(lis)

    for i in range(12):
        for j in range(6):
            if lis[i][j] != ".":        # 글자타입에 따른 bfs
                flag = bfs(lis[i][j], arr, visit, i, j)

                if flag:
                    chainCount += 1     # 만약 bfs로 연쇄가 발생했다면
                    res += 1

    if chainCount == 0:     # 현재 arr에서 연쇄가 안일어났다면
        break

    # bfs 탐색 후 위의 칸에 있는 인덱스 당기기 필요
    changeChained(arr)
    lis = arr


print(res)