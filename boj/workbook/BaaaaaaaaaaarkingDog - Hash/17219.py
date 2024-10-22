n, m = map(int, input().split(" "))
dic = {}

for i in range(n):
    st, pw = map(str, input().split(" "))

    dic[st] = pw

for i in range(m):
    print(dic[input()])