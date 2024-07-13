# A = 순서 뒤집기, D = 첫번째 수 버리기(빈 배열일 경우 오류)
import sys
input = sys.stdin.readline
test = int(input())

for _ in range(test):
    oper = input()
    n = int(input())
    st = input()[1:-1].split(",")
    lis = []

    oper = oper.replace("RR", "")
    flag = 0

    if len(st) != 1:
        lis = list(map(int, st))

        for o in oper:
            if len(lis) == 0:
                flag = 1
                break
            else:
                if o == "D":
                    lis.pop(0)
                else:
                    lis.sort(reverse=True)
    else:       # 배열이 비어있는 경우 error
        flag = 1

    if flag == 1:
        print("error")
    else:
        print(lis)