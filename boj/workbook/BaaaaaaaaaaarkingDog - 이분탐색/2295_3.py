# x+y+z = k -> x+y = k-z

import sys
input = sys.stdin.readline

def binarySearch(number):
    start, end = 0, len(arr)-1

    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == number:
            return True
        elif arr[mid] > number:
            end = mid - 1
        elif arr[mid] <= number:
            start = mid + 1

    return False

n = int(input())
lis = []
arr = []
res = 0

for i in range(n):
    lis.append(int(input()))

for i in range(n):
    for j in range(i, n):
        arr.append(lis[i]+lis[j])

arr.sort()

for i in range(n):
    for j in range(i, n):
        k = lis[j] - lis[i]

        if binarySearch(k):
            res = max(res, lis[j])


print(res)