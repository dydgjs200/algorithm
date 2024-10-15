# 주어진 리스트 중 6개를 뽑는 순열

def backtracking(lotto, idx, path):
    if len(path) == 6:
        print(*path)
        return

    for i in range(idx+1, len(lotto)):
        path.append(lotto[i])
        backtracking(lotto, i, path)
        path.pop()



while True:
    lis = list(map(int, input().split(" ")))
    lotto = lis[1:]

    if lis[0] == 0:
        break

    for i in range(len(lotto)-5):
        backtracking(lotto, i, [lotto[i]])
    print()
