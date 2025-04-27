from collections import deque


def bfs(start):
    que = deque()
    que.append(start)
    visit = [0] * 101
    visit[start] = 1

    while que:
        top = que.popleft()

        if top == 100:
            print(visit[top] - 1)
            return

        for dice in range(1, 7):
            step = top + dice

            if step <= 100:  # 범위 내
                if step not in dic and not visit[step]:  # 사다리나 뱀이 아닐 때
                    que.append(step)
                    visit[step] = visit[top] + 1
                elif step in dic and not visit[dic[step]]:
                    que.append(dic[step])
                    visit[dic[step]] = visit[top] + 1

    return


n, m = map(int, input().split(" "))
dic = {}

for _ in range(n + m):
    a, b = map(int, input().split(" "))
    dic[a] = b

bfs(1)