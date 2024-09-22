from collections import deque
import sys

def cross_check(y, x):
    if lis[y+1][x] == 0 and lis[y][x+1] == 0 and lis[y+1][x+1] == 0:
        return True

    return False

def bfs(y,x,pipe):      # pipe = 0,1,2 -> 가로,세로,대각선
    global cnt
    que = deque()

    que.append((y,x,pipe))

    while que:
        ty, tx, tpipe = que.popleft()

        if ty == n-1 and tx == n-1:
            cnt += 1
            continue        # 모든 경우의 수를 찾아야하므로

        if tpipe == 0:
            if 0 <= tx+1 <= n-1 and lis[ty][tx+1] == 0:
                que.append((ty,tx+1,0))
            if 0 <= ty+1 <= n-1 and 0 <= tx+1 <= n-1:
                if cross_check(ty, tx):
                    que.append((ty+1,tx+1,2))

        elif tpipe == 1:
            if 0 <= ty+1 <= n-1 and lis[ty+1][tx] == 0:
                que.append((ty+1,tx,1))
            if 0 <= ty+1 <= n-1 and 0 <= tx+1 <= n-1:
                if cross_check(ty, tx):
                    que.append((ty+1,tx+1,2))

        elif tpipe == 2:
            if 0 <= tx+1 <= n-1 and lis[ty][tx+1] == 0:
                que.append((ty,tx+1,0))
            if 0 <= ty+1 <= n-1 and lis[ty+1][tx] == 0:
                que.append((ty+1,tx,1))
            if 0 <= ty+1 <= n-1 and 0 <= tx+1 <= n-1:
                if cross_check(ty, tx):
                    que.append((ty+1,tx+1,2))



input = sys.stdin.readline

n = int(input())
lis = []
cnt = 0

for _ in range(n):
    lis.append(list(map(int, input().split(" "))))

bfs(0,1,0)
print(cnt)