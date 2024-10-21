# 계란 = 내구도, 무게

# 계란으로 계란 치기 -> 내구도 = 상대 계란의 무게만큼 감소
# 내구도 <= 0 이면 계란 깨짐

#ex. (a,b) , (c,d) => (a-d, b), (c-b, d)
#ex. (7,5) , (3,4) => (7-4, 5), (3-5, 4) => (3,5), (-2,4)

# 출력 = 얼마나 많은 계란을 깰 수 있는가?

# 1. 현재 인덱스에서 (현재+1, 마지막) 까지 선택 가능..
# recursive(idx) -> recursive(i)

def backtracking(idx, cnt):
    global res

    if idx == n-1:
        res = max(res, cnt)
        return

    if lis[idx][0] <= 0:
        backtracking(idx+1, cnt)
    else:
        for i in range(n):
            if idx == i or lis[i][0] <= 0:
                continue

            lis[idx][0] -= lis[i][1]
            lis[i][0] -= lis[idx][1]
            backtracking(idx+1)
            lis[idx][0] += lis[i][1]
            lis[i][0] += lis[idx][1]


n = int(input())
lis = []
res = 0
visit = [0 for _ in range(n)]

for _ in range(n):
    s, w = map(int, input().split(" "))
    lis.append((s,w))

print(visit)