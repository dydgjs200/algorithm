
# 앞 a, 뒤 b 숫자를 더한 결과 c = a+b
# 10*b + c % 10

num = int(input())
res = num
cnt = 0

while True:
    a, b = divmod(res, 10)
    c = 10*b + (a+b)%10

    cnt += 1
    res = c

    if num == res:
        print(cnt)
        break
