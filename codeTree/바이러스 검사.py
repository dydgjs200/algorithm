import sys

n = 2
lis = [5, 7]
leader, member = 5, 7
res = 0

for l in lis:
    num = l - leader      # 리더를 제외한 고객 수
    res += 1

    if num <= 0:        # 리더 혼자 충분할 때
        continue
    else:
        a, b = divmod(num, member)      # 필요한 팀원 수
        if b == 0:
            res += a
        else:
            res += (a+1)
print(res)