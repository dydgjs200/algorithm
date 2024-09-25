import sys
from collections import deque

# 방향 설정: 북(0), 동(1), 남(2), 서(3)
dx = [-1, 0, 1, 0]  # 행 변화량 (y)
dy = [0, 1, 0, -1]  # 열 변화량 (x)

def bfs(x, y, dir):
    global res
    que = deque()
    que.append((x, y, dir))
    visit[x][y] = 1
    res += 1  # 현재 위치 청소

    while que:
        x, y, dir = que.popleft()
        cleaned = False  # 주변에 청소한 칸이 있는지 여부

        for i in range(4):
            ndir = (dir + 3 - i) % 4  # 반시계 방향으로 회전
            nx = x + dx[ndir]
            ny = y + dy[ndir]

            if 0 <= nx < n and 0 <= ny < m:
                if lis[nx][ny] == 0 and not visit[nx][ny]:
                    visit[nx][ny] = 1
                    res += 1
                    que.append((nx, ny, ndir))
                    cleaned = True
                    break  # 청소할 칸을 찾았으므로 나머지 방향은 탐색하지 않음

        if not cleaned:
            # 후진 시도
            bdir = (dir + 2) % 4  # 후진 방향
            bx = x + dx[bdir]
            by = y + dy[bdir]

            if 0 <= bx < n and 0 <= by < m and lis[bx][by] == 0:
                que.append((bx, by, dir))  # 방향 유지한 채 후진
            else:
                return  # 후진할 곳이 벽이면 종료

n, m = map(int, sys.stdin.readline().split())
x, y, d = map(int, sys.stdin.readline().split())
lis = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visit = [[0]*m for _ in range(n)]
res = 0

bfs(x, y, d)
print(res)
