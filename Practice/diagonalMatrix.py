r,c=map(int,input().split())
mat=[list() for i in range((r+c-1)+(r+c-1))]
l=[input().split() for i in range(r)]
x,y=map(str,input().split())
for i in range(r):
    for j in range(c):
        mat[i-j+c-1].append(l[i][j])
        mat[i+j-c-1].append(l[i][j])
for i in mat:
    if x in i:
        if  y in i:
            print("YES")
            exit()
else:
    print("NO")
