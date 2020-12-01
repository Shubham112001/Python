N=int(input())
l=[input().split()for i in range(N)]
ctr,cctr=0,1
while True:
    s,x=[],[]
    for i in range(0,N-ctr):
        for j in range(0,N):
            if j==ctr  :
                s+=l[i][j]
    x+=l[-cctr]
    s+=x[cctr:]
    if s == s[::-1]:
        print(*s,sep='')
    ctr+=1
    cctr+=1
    if ctr == N-1:
        print(l[0][-1])
        break 
