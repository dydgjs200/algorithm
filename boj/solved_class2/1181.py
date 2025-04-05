n = int(input())
lis = []

for _ in range(n):
    lis.append(input())

s = set(lis)
convert = list(s)
convert = sorted(convert, key=lambda x:(len(x),x))

print('\n'.join(convert))
