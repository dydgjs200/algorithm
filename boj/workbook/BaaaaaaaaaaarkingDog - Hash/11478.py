s = input()
se = set()

for i in range(len(s)):
    for j in range(len(s)-i+1):
        se.add(s[i:i+j])

print(len(se)-1)