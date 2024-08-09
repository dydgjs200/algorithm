# 재료는 아래에서 위로 쌓임
# [야채, 빵, 빵, 야채, 고기, 빵] -> 3~6까지 이용
# [야채, 빵, 야채, 고기, 빵] -> 2~5까지 이용
# 빵,야채,고기,빵 순서가 보존 되어야함. -> ex. 빵,야채,빵,고기 x
# 1231이 되는 부분을 pop

# 1,2,3 -> 빵, 야채, 고기 -> 즉, 문제는 1231이 되는 부분을 pop해야함

def solution(ingredient):
    answer = 0
    lis = []

    for i in ingredient:
        lis.append(i)

        if lis[-4:] == [1, 2, 3, 1]:
            answer += 1

            for j in range(4):
                lis.pop()

    return answer