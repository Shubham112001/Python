r,c=map(int,input().split())
mat=[list(input().split())for i in range(r)]
ch = input()
alp=['d','u','r','l','D','U','R','L']
for i in range(r):
    if ch=='d' or ch=='D':
        print(*mat[-1])
    if ch=='u' or ch=='U':
        print(*mat[0])
    if ch=='r' or ch=='R':
        print((mat[i][c-1]+' ')*c)
    if ch=='l' or ch=='L':
        print((mat[i][0]+' ')*c)
    if ch not in alp:
        print(*mat[i])
