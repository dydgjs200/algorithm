# l개의 소문자, 최소 한개의 모음, 최소 두개의 자음
# 아스키코드가 증가하는 식

mo = ["a", "e", "i", "o", "u"]
def check(inp):        # 모음 개수 출력
    cnt = 0

    for i in inp:
        for m in mo:
            if i == m:
                cnt += 1
                break

    return cnt


def backtracking(path, idx):
    if len(path) == l:
        m = check(path)

        if m >= 1 and len(path) - m >= 2:
            for p in path:
                print(p,end="")

            print()
        return

    for i in range(idx+1, c):
        path.append(alpha[i])
        backtracking(path, i)
        path.pop()



l, c = map(int, input().split(" "))     # l = 백트래킹 depth, c = 글자 종류
alpha = list(map(str, input().split(" ")))
alpha = sorted(alpha)

for i in range(c-l+1):
    backtracking([alpha[i]], i)
