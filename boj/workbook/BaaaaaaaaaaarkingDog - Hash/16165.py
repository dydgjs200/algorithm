import sys
input = sys.stdin.readline

n, m = map(int, input().split())  # n = 걸그룹 수, m = 맞혀야할 문제
dic = {}

for i in range(n):
    team = input().rstrip()
    number = int(input())
    dic[team] = []

    for j in range(number):
        member = input().rstrip()
        dic[team].append(member)

for i in range(m):
    st = input().rstrip()
    kind = int(input())

    if kind == 0:
        # 팀 이름을 입력받으면 팀의 멤버들을 출력
        for member in sorted(dic[st]):
            print(member)
    elif kind == 1:
        # 멤버 이름을 입력받으면 팀 이름을 출력
        for team, members in dic.items():
            if st in members:
                print(team)
                break
