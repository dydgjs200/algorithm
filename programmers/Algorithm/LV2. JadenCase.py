# 공백은 그대로, 숫자가 맨 앞에 있는 문자도 그대로
# 영어로 된 문자는 맨 앞만 대문자 -> 영어가 나왔을 때, 이전 문자가 공백이라면 대문자


def solution(s):
    answer = s[0].upper()

    for i in range(1, len(s)):
        if s[i].isalpha() and s[i - 1] == " ":
            answer += s[i].upper()
        else:
            answer += s[i].lower()

    return answer