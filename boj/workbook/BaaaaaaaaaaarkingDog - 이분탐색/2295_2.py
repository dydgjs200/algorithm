# 세 수를 골라 합한 값 d가 배열에 들어있을 때의 최대값

# 최대값의 범위 = 3 ~ sum(lis)
# 세 수를 뽑고, 이진탐색으로 배열에 존재하는지 확인?
# 시간초과 -> 백트래킹에서 문제가 있는듯..

def recursive(path):
    if len(path) == 3:
        sumArr.append(sum(path))
        return

    for i in range(len(lis)):
        if path[-1] < lis[i]:
            path.append(lis[i])
            recursive(path)
            path.pop()

def binarySearch(number):
    global res
    start, end = 0, len(lis) - 1

    while start <= end:
        mid = (start + end) // 2

        if number == lis[mid]:
            res = max(res, number)
            return
        elif number < lis[mid]:
            end = mid - 1
        elif number >= lis[mid]:
            start = mid + 1

    return

n = int(input())
lis = []
sumArr = []
res = 0

for i in range(n):
    lis.append(int(input()))

lis = sorted(lis)

for i in range(len(lis)):
    recursive([lis[i]])

for i in sumArr:
    binarySearch(i)

print(res)