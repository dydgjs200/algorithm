s = set()
l = set()

for i in range(1, 10001):
    lis = list(str(i))
    add = sum(map(int, lis)) + i
    s.add(add)
    l.add(i)

lis = list(l-s)
lis.sort()

for i in lis:
    print(i)
