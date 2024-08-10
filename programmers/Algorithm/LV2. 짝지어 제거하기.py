def solution(s):
    answer = -1
    lis = [s[0]]

    for i in range(1, len(s)):
        if len(lis) == 0:
            lis.append(s[i])
        else:
            if lis[-1] == s[i]:
                lis.pop()
            else:
                lis.append(s[i])

    return 1 if len(lis) == 0 else 0