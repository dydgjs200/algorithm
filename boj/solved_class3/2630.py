# 타일은 파란색 1, 하얀색 0
# 나눈 부분이 모두 같은 색이 아니라면 n/2로 나눔
# 결과적으로 나눠진 부분의 하얀색, 파란색 영역 순으로 출력

# 1,2,3,4분면의 영역을 나눔 -> 나눈 영역을 색깔 체크 -> 색깔이 다를 시 재귀반복

def recursive(x, y, N):
    global blue, white
    color = lis[x][y]
    for i in range(x, x+N):
        for j in range(y, y+N):
            if color != lis[i][j]:
                recursive(x,y,N//2)
                recursive(x,y+N//2, N//2)
                recursive(x+N//2, y, N//2)
                recursive(x+N//2, y+N//2, N//2)
                return
    if color == 0:
        white += 1
    else:
        blue += 1


n = int(input())
lis = [list(map(int, input().split(" "))) for _ in range(n)]
blue, white = 0, 0

recursive(0,0, n)
print(white)
print(blue)