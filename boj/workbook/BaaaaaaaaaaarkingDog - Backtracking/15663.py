
# 첫 인덱스는 중복이 안되게 뽑아야함 -> set(sl 배열)
# 다음부터는 입력받은 lis의 갯수에 맞게 뽑아야함..

from collections import Counter

def backtracking(path):
    if len(path) == m:
        print(*path)
        return

    for i in range(n):
        path.append(lis[i])
        backtracking(path)
        path.pop()

n, m = map(int, input().split(" "))
lis = list(map(int, input().split(" ")))

sl = list(set(lis))
sl = sorted(sl)
lis = sorted(lis)

dic = Counter(lis)

print(dic)

for i in range(len(sl)):
    backtracking([sl[i]])