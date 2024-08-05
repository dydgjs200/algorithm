# keymap 원소에 있는 모든 문자열을 쓸 수 있음 -> ["a", "abc", "de"] 라면 a,b,c,d,e가 모두 가능


def solution(keymap, targets):
    answer = []
    dic = {}  # {"key" : idx}

    for k in keymap:
        for i in range(len(k)):
            if k[i] not in dic:
                dic[k[i]] = i + 1
            else:
                dic[k[i]] = min(dic[k[i]], i + 1)

    # dic = {a:1, b:1 .. }

    for t in targets:
        res = 0
        flag = True
        for i in range(len(t)):
            if t[i] not in dic:
                flag = False
                break
            else:
                res += dic[t[i]]
        if flag:
            answer.append(res)
        else:
            answer.append(-1)

    return answer