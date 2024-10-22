# 입출 주어질 때, 현재 회사에 있는 사람 역순 출력

n = int(input())
dic = {}
cnt = 0

for _ in range(n):
    name, move = map(str, input().split(" "))

    dic[name] = move

lis = [k for k, v in dic.items() if v == "enter"]
lis = sorted(lis, reverse=True)

for l in lis:
    print(l)

