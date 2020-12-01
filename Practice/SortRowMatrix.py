def evencount(val):
    ctr = 0
    for i in val:
        if i%2 == 0:
            ctr += 1
        return ctr
r,c=map(int,input().split())
mat=[list(input().split())for i in range(r)]
mat = sorted(mat, key=evencount)
for i in mat:
    print(*i)