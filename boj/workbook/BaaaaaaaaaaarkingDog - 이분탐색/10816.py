
from collections import Counter

def binary(number):
    start, end = 0, len(lis)-1

    while start <= end:
        mid = (start + end) // 2

        if lis[mid] == number:
            return 1
        elif lis[mid] > number:
            end = mid - 1
        elif lis[mid] <= number:
            start = mid + 1

    return 0

n = int(input())
lis = list(map(int, input().split(" ")))
m = int(input())
find = list(map(int, input().split(" ")))

lis = sorted(lis)

c = Counter(lis)

for i in find:
    if binary(i):
        print(c[i], end=" ")
    else:
        print(0, end=" ")
