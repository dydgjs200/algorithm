
def recursive(idx, cnt):
    global ans
    if idx >= n-1:
        ans = max(cnt, ans)
        return

    for i in range(idx, n):
        if lis[idx][1] <= lis[i][0]:
            recursive(i+1, cnt+1)



n = int(input())
lis = []
ans = 0

# 입력값이 정렬되어 있지 않다.

for _ in range(n):
    a, b = map(int, input().split(" "))
    lis.append((a,b))

lis.sort(key=lambda x:x[1])

for i in range(n-1):
    recursive(i, 1)

print(ans)
