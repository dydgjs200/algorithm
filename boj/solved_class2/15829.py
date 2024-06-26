n = int(input())
s = input()
pos = 0
r = 0

for i in s:
    r += (ord(i) - ord("a") + 1) * (pow(31, pos))
    pos += 1

print(r % 1234567891)