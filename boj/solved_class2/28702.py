for i in range(3):
    s = input()
    res = 0

    if s.isnumeric():
        res = int(s) + 3 - i

        if res % 15 == 0:
            print("FizzBuzz")
        elif res % 3 == 0:
            print("Fizz")
        elif res % 5 == 0:
            print("Buzz")
        else:
            print(res)

        break
