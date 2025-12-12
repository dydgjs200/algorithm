test = int(input())

for t in range(test):
    inp = input()
    score = 0
    cnt = 1

    for i in inp:
        if i == 'O':
            score += cnt
            cnt += 1
        else:
            cnt = 1

    print(score)
