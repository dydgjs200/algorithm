# 두 개의 나무 중 움직이며 사과를 먹어야함.
# 최대 w 횟수만큼만 움직일 것
# 1번나무에서 시작

# tc1 -> 1번 고정 -> 11 받고 -> 2번 이동 -> 22 받고 -> 1번 이동 -> 11 받고 = 6개


# 출력 = 받을 수 있는 자두의 최대

# w = 움직일 횟수, lis = 떨어지는 나무 정보

def recursive(depth, tree, move, eat):     # 이동 한다 안한다의 최대
    global count

    if depth == t:
        count = max(count, eat)
        return
    if lis[depth] == tree:  # 현재 위치가 나무 밑일 경우
        eat += 1

    recursive(depth + 1, tree, move, eat)

    if move < w:        # 이동 횟수가 남았을 때,
        if tree == 1:
            recursive(depth+1, 2, move+1, eat)
        else:
            recursive(depth+1, 1, move+1, eat)

t, w = map(int, input().split(" "))
lis = []
count = 0       # w까지 가능

for i in range(t):
    lis.append(int(input()))

recursive(0, 1, 0, 0)
print(count)