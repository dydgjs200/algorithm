lis = list(map(int, input().split(" ")))
number = [i for i in range(1, 9)]

if lis == number:
    print("ascending")
elif lis == sorted(number, reverse=True):
    print("descending")
else:
    print("mixed")