# 같은 색이 4개 이상 상하좌유 연결 시 터짐 -> 테트리스처럼 위에 있던 애들이 내려옴
# 상대방의 필드가 주어질 때 연쇄가 몇번일지?

# 1. 주어진 맵에서 연쇄를 찾음
# 2. 연쇄를 제거하고, 위의 칸을 아래로 이동 (턴을 생각해야할듯..)

# bfs로 연쇄들을 찾고 제거 -> 한칸씩 아래로 당김 -> 이걸 반복.
# bfs를 한칸씩 해주면 될듯!

mx = [1, -1, 0, 0]
my = [0, 0, -1, 1]

from collections import deque

def bfs(charType, visit, y, x):
    que = deque()
    que.append((y,x))
    visit[y][x] = 1
    cnt = 0         # 연쇄 개수는 4개 이상!

    while que:
        ty, tx = que.popleft()






lis = []
isChained = True      # 리스트에 연쇄가 존재하지 않을 시 종료
charType = ["R", "G", "B", "P", "Y"]        # 글자 타입

for _ in range(12):
    l = list(map(str, input()))
    lis.append(l)

while isChained:        # 연쇄가 없다면 종료
    chainCount = 0      # 연쇄의 개수

    visit = [[0 for _ in range(6)] for _ in range(12)]      # 연쇄 후 당기기 함수 다음 초기화

    for t in charType:
        for i in range(12):
            for j in range(6):
                if lis[i][j] == t and not visit[i][j]:
                    bfs(t, visit, i, j)



    # bfs 탐색 후 위의 칸에 있는 인덱스 당기기 필요
