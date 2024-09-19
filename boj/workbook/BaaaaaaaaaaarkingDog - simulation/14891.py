from collections import deque

def move(lis, dir):
    if dir == -1:        # 반시계일 때
        lis.append(lis.popleft())
    elif dir == 1:       # 시계일 때
        lis.appendleft(lis.pop())
    return lis

def rotate_all(num, dir):
    # 회전 여부와 방향을 기록할 리스트
    rotate = [0] * 4
    rotate[num] = dir

    # 왼쪽 톱니바퀴 체크
    for i in range(num, 0, -1):
        if lis[i][6] != lis[i-1][2]:
            rotate[i-1] = -rotate[i]
        else:
            break

    # 오른쪽 톱니바퀴 체크
    for i in range(num, 3):
        if lis[i][2] != lis[i+1][6]:
            rotate[i+1] = -rotate[i]
        else:
            break

    # 기록된 방향에 맞춰 톱니바퀴 회전
    for i in range(4):
        if rotate[i] != 0:
            lis[i] = move(lis[i], rotate[i])

def score():
    result = 0
    for i in range(4):
        if lis[i][0] == 1:
            result += 2**i
    return result

# 초기 톱니바퀴 상태 입력
lis = []
for i in range(4):
    lis.append(deque(map(int, input())))

k = int(input())  # 회전 횟수 입력
for _ in range(k):
    num, dir = map(int, input().split())  # 톱니 번호와 방향 입력
    rotate_all(num-1, dir)  # num-1로 배열 인덱스 맞춤

# 최종 점수 출력
print(score())
