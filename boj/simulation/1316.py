import re

t = int(input())
res = 0

for _ in range(t):
    inp = input()
    flag = 0        # 0 = 체커 단어

    for i in range(len(inp)):
        last_index = i
        for j in range(i+1, len(inp)):
            if inp[i] == inp[j]:
                if last_index == j-1:       # 현재 글자가 이전 글자와 같다면
                    last_index = j
                    continue
                else:
                    flag = 1
                    break

    if flag == 0:
        res += 1

print(res)