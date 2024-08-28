import sys
input = sys.stdin.readline

def binarySearch(number):
    start, end = 0, len(lis) - 1

    while start <= end:
        mid = (start + end) // 2

        if lis[mid] == number:
            return mid
        elif lis[mid] <= number:
            start = mid+1
        else:
            end = mid - 1

    return -1

n = int(input())
lis = list(map(int, input().split(" ")))        # 1 2 3 4 5
m = int(input())
find = list(map(int, input().split(" ")))

lis = sorted(lis)       # 이분탐색을 위한 정렬

for i in find:
    if binarySearch(i) != -1:
        print(1)
    else:
        print(0)