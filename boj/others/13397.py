# 구간의 점수 = 최대 - 최소
# 이진 탐색을 이용해, 구간의 점수가 mid 값을 넘을 때 새 구간 설정
# 투 포인터를 이용해 구간을 설정

import sys
input = sys.stdin.readline

def divide(mid, lis, n):        # mid 값을 중심으로 구간을 나눠지는지 판단하는 함수
    count = 1       # 구간의 갯수
    min_value = lis[0]
    max_value = lis[0]

    for i in range(1, len(lis)):        # 배열을 순회하며 구간을 설정
        min_value = min(min_value, lis[i])
        max_value = max(max_value, lis[i])

        if max_value - min_value > mid:
            count += 1
            min_value = lis[i]
            max_value = lis[i]

    return count <= n

def binarySearch(lis, n):
    low = 0
    high = max(lis) - min(lis)      # mid의 범위 = 0~(배열 최대 - 최소)

    while low < high:
        mid = (low + high) // 2
        if divide(mid, lis, n):
            high = mid
        else:
            low = mid+1

    return low

n, m = map(int, input().split(" "))
lis = list(map(int, input().split(" ")))

print(binarySearch(lis, m))

