# r1. 2개의 세력(이다솜, 임도연), 7명을 뽑아야함 (자리는 상하좌우 인접)
# r2. 뽑은 리스트는 (이다솜 > 임도연)을 만족

# 7개의 좌표를 백트래킹으로 뽑음 -> bfs가 안되는 이유는 T자로 선택이 될수도있기 때문
# 뽑은 좌표들 중 r2를 만족하면 카운트

# 해결 못한 코드임.!!!!!!!!!!!!

mx = [1, -1, 0, 0]
my = [0, 0, -1, 1]

def count_team(path):
    s, y = 0, 0     # 이다솜, 임다연 파 카운트

    for p in path:
        px, py = p[0], p[1]

        if lis[px][py] == "S":
            s += 1
        else:
            y += 1

    if s >= 4:
        return True
    else:
        return False

def backtracking(path, i, j, visit):
    global res

    if len(path) == 7:
        if count_team(path):
            #print(*path)
            res += 1
        return

    for k in range(4):
        dx = mx[k] + i
        dy = my[k] + j

        if 0 <= dx < 5 and 0 <= dy < 5 and not visit[dx][dy]:
            visit[dx][dy] = 1
            path.append((dx, dy))
            backtracking(path, dx, dy, visit)
            visit[dx][dy] = 0
            path.pop()



lis = []
res = 0     # 정답 카운트

for i in range(5):
    lis.append(input())

for i in range(5):
    visit = [[0 for _ in range(5)] for _ in range(5)]
    for j in range(5):
        visit[i][j] = 1
        backtracking([(i, j)], i, j, visit)

print(res)