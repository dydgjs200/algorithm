# n종류를 이용해서 k 금액을 만드는 최소개수
# 그리디? -> 가장 큰 종류의 동전부터 k금액을 채워나가자

n, k = map(int, input().split(" "))
lis = []
cnt = 0

for _ in range(n):
    lis.append(int(input()))

for i in range(n-1, -1, -1):
    if k >= lis[i]:
        a, b = divmod(k, lis[i])
        k = b
        cnt += a

print(cnt)