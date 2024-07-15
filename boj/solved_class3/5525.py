# n = 패턴의 길이, m = 문자열 길이, s = 문자열

n = int(input())
m = int(input())
s = input()
cnt = 0

pattern = "I"

for i in range(n):
    pattern += "OI"

for i in range(m-len(pattern)+1):
    spl = s[i:i+len(pattern)]

    if spl == pattern:
        cnt += 1

print(cnt)

st = s.replace(pattern, "K")
print(st)