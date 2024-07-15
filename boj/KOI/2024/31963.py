# 어떠한 배열이 주어지고 임의의 항에 대해 *2 연산을 하여 오름차순 만들기
# 연산의 최소 횟수(bfs, dp 등을 생각해보자)

# 오름차순 -> 앞에서부터 만들기


n = int(input())
lis = list(map(int, input().split(" ")))
cnt = 0

start = lis[0]

for i in range(1, n):
    if start >= lis[i]:
        while lis[i] < start:
            lis[i] *= 2
        start = lis[i]

print(lis)
