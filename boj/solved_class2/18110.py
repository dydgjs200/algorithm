# 절사평균 = 30% 값 제외 (상단 15%, 하단 15% 제외) 일 때
# 절사평균 값이 소수일 경우 반올림

n = int(input())

if n == 0:
    print(0)
else:
    avgCut = round(n * 0.15)

    lis = []

    for i in range(n):
        lis.append(int(input()))

    lis.sort()
    cut = lis[avgCut:len(lis) - avgCut]
    res = sum(cut) / len(cut)
    print(round(res))