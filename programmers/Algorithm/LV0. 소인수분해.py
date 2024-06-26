def find(n):
    res = []
    for i in range(2, n // 2 + 1):
        for j in range(i + i, n + 1, i):
            if j not in res:
                res.append(j)

    return [i for i in range(2, n + 1) if i not in res]


def solution(n):
    r = find(n)

    answer = [i for i in r if n % i == 0]

    return answer