# 다음층은 현재층의 왼쪽 or 오른쪽만 선택 가능

n = int(input())
lis = []

for _ in range(n):
    lis.append(list(map(int, input().split(" "))))

for i in range(1, n):
    for j in range(len(lis[i])):
        if j == 0:
            lis[i][j] = lis[i-1][j] + lis[i][j]
        elif j == len(lis[i]) - 1:
            lis[i][j] = lis[i][j] + lis[i-1][j-1]
        else:
            lis[i][j] = max(lis[i-1][j-1], lis[i-1][j]) + lis[i][j]

print(max(lis[n-1]))