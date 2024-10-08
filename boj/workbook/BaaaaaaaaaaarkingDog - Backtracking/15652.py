# 여러번 수를 고를 때, 오름차순?

def backtracking(path):
    if len(path) == m:
        print(*path)
        return

    for i in range(1, n+1):
        if path[-1] <= i:
            path.append(i)
            backtracking(path)
            path.pop()

n, m = map(int, input().split(" "))

for i in range(1, n+1):
    backtracking([i])
