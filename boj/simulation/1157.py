# 가장 많이 사용된 알파벳 출력 (여러개일 시 ? 출력)

from collections import Counter

def sol(inp):
    inp = inp.upper()
    count = Counter(inp)
    lis = sorted(count.items(), key=lambda x: x[1], reverse=True)

    if len(lis) <= 1:
        return print(inp[0])

    if lis[0][1] == lis[1][1]:
        return print("?")
    else:
        return print(lis[0][0])


inp = input()
sol(inp)