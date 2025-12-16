number = int(input())
lis = []

for i in range(number):
    a, b = map(int, input().split(" "))
    lis.append([a,b])

lis = sorted(lis, key= lambda x:(x[0], x[1]), reverse=True)

print(lis)