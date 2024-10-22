# dic = {학번 : 순위}
import sys
input = sys.stdin.readline

n, m = map(int, input().split(" "))
dic = {}
cnt = 0

for i in range(m):
    dic[sys.stdin.readline().rstrip()] = i

lis = sorted(dic.items(), key=lambda x:x[1])

if len(lis) < n:
    n = len(lis)

for i in range(n):
    print(lis[i][0])