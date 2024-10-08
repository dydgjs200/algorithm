# 같은 수를 여러번 골라도 된다.

def backtracking(path):
    if len(path) == m:
        print(*path)
        return

    for i in range(1, n+1):
        path.append(i)
        backtracking(path)
        path.pop()

n, m = map(int, input().split(" "))

for i in range(1, n+1):
    backtracking([i])