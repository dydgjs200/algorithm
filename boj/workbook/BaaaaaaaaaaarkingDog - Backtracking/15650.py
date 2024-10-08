# 1~n까지 m을 중복없이 고름
# 오름차순

def backtracking(start, path):
    if len(path) == m:
        print(*path)
        return

    for i in range(start+1, n+1):
        if path[-1] < i:
            path.append(i)
            backtracking(i, path)
            path.pop()

n, m = map(int, input().split(" "))

for i in range(1, n+1):
    backtracking(i, [i])