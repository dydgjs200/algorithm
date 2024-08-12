# 2명씩 탈 수 있을 때, 최소의 값 -> 최소+최대 < limit
# 즉, binarySearch

def solution(people, limit):
    answer = 0
    start, end = 0, len(people) - 1
    people = sorted(people)

    while start <= end:
        if people[start] + people[end] <= limit:
            start += 1
            end -= 1
        else:
            end -= 1
        answer += 1

    return answer