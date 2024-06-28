import sys

# 입력 숫자면 포켓몬, 포켓몬이라면 숫자를 리턴
n, m = map(int, input().split(" "))
dic = {}
dic2 = {}

for i in range(n):
    s = sys.stdin.readline().strip()
    dic[s] = i + 1
    dic2[i+1] = s


for i in range(m):
    question = sys.stdin.readline().strip()

    if not question.isnumeric():
        print(dic[question])
    else:
        print(dic2[int(question)])