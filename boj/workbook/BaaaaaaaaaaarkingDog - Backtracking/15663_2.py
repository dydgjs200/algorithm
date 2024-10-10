def backtracking(path, lis, visit):
    global res
    prev = -1        # 이전 값

    if len(path) == m:
        res.append(path[:])
        return

    for i in range(n):
        # 같은 인덱스를 두 번 방문하지 않고, 이전 값과 중복되지 않도록 처리
        if not visit[i] and lis[i] != prev:
            prev = lis[i]          # 현재 값이 이전 값과 다르면 prev를 갱신
            visit[i] = 1           # 현재 인덱스를 방문했다고 표시
            path.append(lis[i])    # 현재 값을 경로에 추가
            backtracking(path, lis, visit)  # 재귀 호출로 백트래킹 수행
            visit[i] = 0           # 돌아오면 방문 표시를 해제
            path.pop()             # 경로에서 현재 값을 제거


n, m = map(int, input().split(" "))
lis = list(map(int, input().split(" ")))
res = []

# 입력 리스트를 정렬하여 중복 처리를 쉽게 만듦
lis.sort()

# 방문 여부를 관리하는 visit 배열
visit = [0 for _ in range(n)]

# 백트래킹 호출
backtracking([], lis, visit)

# 결과 출력
for r in res:
    print(*r)
