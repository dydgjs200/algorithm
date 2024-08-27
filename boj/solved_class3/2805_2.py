# m 만큼의 나무만을 가져가야함 -> 자르는 값 k의 최대값
# k의 범위 = 1 ~ 배열의 최대값
# 즉 mid를 중심으로 잘랐을 때 남는 여분의 합이 m이 되도록

def binarySearch(lis):
    low = 1
    high = max(lis)

    while low <= high:
        mid = (low + high) // 2
        l = 0       # 기준값을 중심으로 자르고 남은 값의 합

        for i in lis:
            if i >= mid:
                l += (i - mid)

        if l >= m:
            low = mid + 1
        else:
            high = mid - 1

    return high

n, m = map(int, input().split(" "))
lis = list(map(int, input().split(" ")))

print(binarySearch(lis))

