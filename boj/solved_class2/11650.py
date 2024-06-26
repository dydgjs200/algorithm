n = int(input())
area = []

for i in range(n):
    a, b = map(int, input().split(" "))
    area.append((a,b))

area.sort(key=lambda x:(x[0], x[1]))

for a in area:
    print(*a)