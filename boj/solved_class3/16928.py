from collections import deque

def bfs(start):
    que = deque()
    que.append(start)
    visited[start] = 0  # 시작 위치의 이동 횟수를 0으로 설정

    while que:
        top = que.popleft()

        # 현재 위치가 100이면 이동 횟수를 반환
        if top == 100:
            print(visited[top])
            return

        for i in range(1, 7):  # 주사위 범위 1~6
            move = top + i

            if move <= 100 and visited[move] == -1:  # 범위 내이고 방문하지 않은 경우
                if move in up:
                    move = up[move]  # 사다리 타고 올라가기
                elif move in down:
                    move = down[move]  # 뱀 타고 내려가기

                if visited[move] == -1:  # 이동한 위치가 방문되지 않은 경우
                    visited[move] = visited[top] + 1
                    que.append(move)

n, m = map(int, input().split())
up = {}
down = {}

visited = [-1] * 101  # 방문 배열을 -1로 초기화

for _ in range(n):
    a, b = map(int, input().split())
    up[a] = b

for _ in range(m):
    a, b = map(int, input().split())
    down[a] = b

bfs(1)
