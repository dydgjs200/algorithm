inp = input()
cnt = 0
lis = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
st = inp

for l in lis:
    st = st.replace(l, "*")

print(len(st))