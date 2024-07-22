# 테트로미노를 하나 놓았을 때 최대값?
# 즉, 붙어있는 4칸의 최대 합
# 백트래킹을 통해 한칸씩 최대 값을 찾기

# ㅜ,ㅗ,ㅏ,ㅓ 모양은 일반적인 DFS로 해결되지 않으므로 그것을 따로 처리해야함.
# 두 칸을 탐색할 경우, 거기서 다시 재귀로 또 탐색
# 세 칸까지 탐색할 경우 다음칸 탐색할 때 종료되므로 위의 모양탐색이 되지 않음.
import sys


input = sys.stdin.readline

mx = [1,-1,0,0]
my = [0,0,-1,1]

# 4칸을 선택하는 모든 경우의 수
def dfs(x, y, sumVal, cnt):
    global res
    if cnt == 4:
        if res <= sumVal:
            res = sumVal
        return

    for i in range(4):
        dx = mx[i] + x
        dy = my[i] + y

        if 0 <= dx < n and 0 <= dy < m:
            if not visit[dx][dy]:
                visit[dx][dy] = 1
                if cnt == 2:
                    dfs(x, y, sumVal+lis[dx][dy], cnt+1)
                dfs(dx,dy,sumVal+lis[dx][dy], cnt+1)
                visit[dx][dy] = 0


n, m = map(int, input().split(" "))
lis = []
res = 0

for _ in range(n):
    lis.append(list(map(int, input().split(" "))))

visit = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        visit[i][j] = 1
        dfs(i,j,lis[i][j], 1)
        visit[i][j] = 0

print(res)