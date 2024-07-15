# n개 버스 중 하나를 선택해서 x 이내로 도착해야함
# 버스가 출발하는데 걸리는 시간 S, 학교까지 가는 시간 T
# 정답 여러개이면 가장 늦게 출발하는 버스

n, x = map(int, input().split(" "))
lis = []

for i in range(n):
    a, b = map(int, input().split(" "))

    if a+b <= x:
        lis.append([a,b])

if len(lis) == 0:
    print(-1)
else:
    lis.sort(key=lambda x:x[0], reverse=True)
    print(lis[0][0])