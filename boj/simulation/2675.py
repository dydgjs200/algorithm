# R = 각 문자 반복횟수

test = int(input())

for _ in range(test):
    number, inp = input().split(" ")
    st = ""

    for i in range(len(inp)):
        for j in range(int(number)):
            st += inp[i]


    print(st)