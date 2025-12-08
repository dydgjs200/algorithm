# 적절한 괄호로 최소값 만들기
# 중첩 괄호 고려 필요 x (덧셈, 뺄셈만이여서)
# 최소 = - 이전의 +값을 모두 더한 뒤 빼줘야함

s = input().split('-')
answer = 0
for i in range(len(s)):
    temp_sum = sum(map(int, s[i].split('+')))
    if i == 0:
        answer += temp_sum
    else:
        answer -= temp_sum
print(answer)