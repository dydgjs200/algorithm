# 중복 알파벳은 가장 처음 값으로 출력
# 해당 글자의 인덱스 값을 알파벳 배열 위치에 저장

inp = input()
alpha = [-1] * 26

for i in range(len(inp)):
    idx = ord(inp[i]) - ord("z") + 25

    if alpha[idx] == -1:
        alpha[idx] = i

print(*alpha)
