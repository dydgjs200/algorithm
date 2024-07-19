# 옷 조합을 입지 않는다 -> 조합 문제
# 경우의 수 = 항목을 선택하지 않는 경우 1을 추가한 -> (항목+1) * 분류 - 1

t = int(input())

for _ in range(t):
    n = int(input())
    dic = {}

    for i in range(n):
        name, classification = map(str, input().split(" "))

        if classification not in dic:
            dic[classification] = 1
        else:
            dic[classification] += 1

    count = 1

    for k,v in dic.items():
        count *= (v+1)

    print(count-1)




