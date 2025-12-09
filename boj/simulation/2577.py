cal = 1
number = [0] * 10

for i in range(3):
    cal *= int(input())

for i in str(cal):
    number[int(i) - 10] += 1

for _ in number:
    print(_)