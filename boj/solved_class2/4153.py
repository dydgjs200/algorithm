while True:
    lis = list(map(int, input().split(" ")))

    if sum(lis) == 0:
        break

    max_idx = lis.index(max(lis))
    res = 0

    for i in range(3):
        if i != max_idx:
            res += pow(lis[i], 2)


    if res == pow(lis[max_idx], 2):
        print("right")
    else:
        print("wrong")