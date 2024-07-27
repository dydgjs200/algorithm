n = int(input())

for _ in range(n):
    n, m = map(int, input().split(" "))     # m은 궁금한 문서의 인덱스번호
    cnt = 0
    pos = m

    # dic -> 인덱스 : 중요도
    lis = list(map(int, input().split(" ")))

    while True:
        if len(lis) == 1:
            print(cnt+1)
            break
        if pos == 0 and lis[pos] > max(lis[1:]):
            print(cnt)
            break
        else:
            if lis[0] > max(lis[1:]):
                lis.pop(0)
                if pos == 0:
                    pos = len(lis) - 1
                else:
                    pos -= 1
            else:
                t = lis.pop(0)
                lis.append(t)

