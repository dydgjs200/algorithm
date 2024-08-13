# 6,8 => 6 12 18 24 / 8 16 24 -> gcd(a,b) == n -> a//n * b

def solution(arr):
    from math import gcd

    if len(arr) == 1:  # 길이 1일때는 해당 원소 한개
        return arr[0]
    # temp = arr[0] // gcd(arr[0],arr[1]) * arr[1]
    temp = 0
    for i in range(2, len(arr)):
        temp = temp // gcd(temp, arr[i]) * arr[i]

    return temp