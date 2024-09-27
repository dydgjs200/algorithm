lis = [input() for _ in range(3)]
num = 0
idx = 0

for i in range(len(lis)):       # 맨 마지막으로 숫자가 나오는 것을 찾기
    if lis[i].isnumeric():
        num = int(lis[i])
        idx = i     # idx = 0~2

if idx == 0:
    res = num + 3
elif idx == 1:
    res = num + 2
elif idx == 2:
    res = num + 1

if res % 15 == 0:
    print("FizzBuzz")
elif res % 3 == 0:
    print("Fizz")
elif res % 5 == 0:
    print("Buzz")
else:
    print(res)



