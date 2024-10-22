import sys

input = sys.stdin.readline

n, m = map(int, input().split(" "))
dic = {}

for i in range(1, n+1):
    dic[input()] = i

for j in range(m):
    name = input()

    for k, v in dic.items():
        if name.isnumeric() and v == int(name):
            print(k)
        elif k == name:
            print(dic[k])


