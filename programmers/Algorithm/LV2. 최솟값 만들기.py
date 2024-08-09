# 배열 a,b에서 각 원소들을 곱한 값의 누적이 가장 작아야함.
# 즉, 각 곱연산에서 가장 작은 값들만 선택
# 두 원소를 고를때는 가장 작은 값 * 가장 큰 값 -> a 원소에서 가장 작은 값, b 원소에서 가장 큰 값

def solution(A, B):
    answer = 0

    A = sorted(A)
    B = sorted(B, reverse=True)

    for i in range(len(A)):
        answer += (A[i] * B[i])

    return answer