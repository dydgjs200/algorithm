# x의 0 제거
# 제거된 문자열의 길이를 2진법
# 위 과정을 1이 될 때 까지 반복

# 출력 = [변환횟수, 0 제거 갯수]

from collections import Counter


def solution(s):
    answer = []
    convert, zero = 0, 0  # 출력 = 변환횟수, 0 제거 갯수

    while s != "1":
        c = Counter(s)
        zero += c["0"]
        convert += 1
        s = ''.join(["1" for i in range(c["1"])])

        s = bin(len(s))[2:]

    return [convert, zero]