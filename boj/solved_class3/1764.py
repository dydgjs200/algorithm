n, m = map(int, input().split(" "))
lis = [input() for _ in range(n+m)]
name1 = lis[:n]
name2 = lis[n:]

s = set.intersection(set(name1), set(name2))
s = sorted(s)
print(len(s))

for i in s:
    print(i)