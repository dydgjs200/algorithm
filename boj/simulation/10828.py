import sys

# input() 대신 sys.stdin.readline()을 사용하면 입력 속도가 빨라져 백준에서 유리합니다.
input = sys.stdin.readline

num = int(input())
lis = []  # 리스트를 스택으로 사용

for i in range(num):
    # 한 줄 전체를 읽습니다. (예: "push 1" 또는 "top")
    command_line = input().split()

    # 명령어 (oper)와 요소 (element) 분리
    oper = command_line[0]  # 명령어는 첫 번째 요소

    if oper == "push":
        # push 명령은 항상 두 번째 요소(element)를 가지고 있습니다.
        element = command_line[1]
        lis.append(element)

    elif oper == "pop":
        if not lis:  # if len(lis) == 0: 와 동일
            print("-1")
        else:
            # 스택의 끝(가장 오른쪽) 요소를 꺼냅니다. (LIFO 원칙)
            print(lis.pop())

    elif oper == "size":
        print(len(lis))

    elif oper == "empty":
        if not lis:
            print(1)  # 비어 있으면 1
        else:
            print(0)  # 비어 있지 않으면 0

    elif oper == "top":
        if not lis:
            print("-1")
        else:
            # 스택의 끝(가장 오른쪽) 요소를 확인합니다.
            # lis[-1]은 리스트의 마지막 요소를 가리킵니다.
            print(lis[-1])