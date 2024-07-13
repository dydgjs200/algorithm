# m만큼 가져가기 위해 필요한 높이 h
# 이분탐색을 통해 h를 최소로 탐색함
# h의 범위는 입력받은 나무의 1 ~ 최대값

def binarySearch(lis):
    start, end = 1, max(lis)

    while start <= end:
        half = (start+end) // 2
        cut = 0

        for i in lis:
            if i >= half:
                cut += (i - half)

        if cut >= m:
            start = half + 1
        else:
            end = half - 1

    return end




n, m = map(int, input().split(" "))
lis = list(map(int, input().split(" ")))

print(binarySearch(lis))
