
def backtracking(path):
    if len(path) == m:
        print(*path)
        return

    for i in range(n):
        if path[-1] != lis[i] and lis[i] not in path:
            path.append(lis[i])
            backtracking(path)
            path.pop()

n, m = map(int, input().split(" "))
lis = list(map(int, input().split(" ")))

lis = sorted(lis)

for i in range(n):
    backtracking([lis[i]])
