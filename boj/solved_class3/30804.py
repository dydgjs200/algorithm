def pointer(lis, k):
    cnt = 0
    l, r = 0, 0
    current_sum = lis[0]

    while r <= len(lis):
        if current_sum == k:
            cnt += 1
            current_sum -= lis[l]
            l += 1
            break
        elif current_sum < k:
            r += 1
            current_sum += lis[r]
        else:
            l += 1
            current_sum -= lis[l]

    return cnt

n, m = map(int, input().split(" "))
lis = list(map(int, input().split(" ")))

res = pointer(lis, m)
print(res)
