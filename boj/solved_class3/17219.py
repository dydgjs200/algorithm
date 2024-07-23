n, m = map(int, input().split(" "))
dic = {}


for _ in range(n):
    path, password = map(str, input().split(" "))
    dic[path] = password

for _ in range(m):
    find = input()
    print(dic[find])
