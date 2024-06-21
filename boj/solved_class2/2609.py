a, b = map(int, input().split(" "))
res1, res2 = 0, 0

# 최대 공약수
for i in range(b, -1, -1):
    if a % i == 0 and b % i == 0:
        res1 = i
        break

# 최소 공배수
res2 = (a * b) // res1

print(res1, res2)