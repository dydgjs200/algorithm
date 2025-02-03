r = 1
num = [0] * 10

for i in range(3):
    r *= int(input())

rs = str(r)

for s in rs:
    num[int(s)] += 1

for n in num:
    print(n)