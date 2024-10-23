import sys
input = sys.stdin.readline

def changeTime(time):  # 시간을 분으로 변환
    h, m = map(int, time.split(":"))
    return h * 60 + m

s, e, q = map(str, sys.stdin.readline().split())
res = 0

ans = set()

s = changeTime(s)
e = changeTime(e)
q = changeTime(q)


while True:
    try:
        time, name = input().split()
        t = changeTime(time)

        if t <= s:
            ans.add(name)

        if e <= t <= q and name in ans:     # 입장했어야만 퇴장할 때 여부에서 체크 가능
            res += 1
            ans.remove(name)
    except:
        break

print(res)
