st = input()
alpha = [-1] * 26
index = 0

for s in st:
    idx = ord(s) - ord("a")

    if alpha[idx] == -1:
        alpha[idx] = index

    index += 1

print(" ".join(map(str, alpha)))