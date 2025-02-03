s = input()
s = s.strip(" ")

st = s.replace(" ", "")
if len(st) == 0:
    print(0)
else:
    print(len(s.split(" ")))