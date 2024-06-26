n = int(input())
arr1 = list(map(int, input().split(" ")))
m = int(input())
arr2 = list(map(int, input().split(" ")))
dic = {}

for i in arr1:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1

for r in arr2:
    if r not in dic:
        print(0, end=" ")
    else:
        print(dic[r], end=" ")