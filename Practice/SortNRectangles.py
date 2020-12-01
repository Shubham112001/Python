N=int(input())
l=[]
b=[]
a=[]
c=[]
for i in range(N):
    L,B=input().split(" ")
    l.append(L)
    b.append(B)
for i in range(N):
    Area=int(l[i])*int(b[i])
    a.append(Area)
a.sort()
for i in range(N):
    if (int(l[i])*int(b[i]))==int(a[i]) and l[i] not in c and b[i] not in c:
        print(*str(l[i]),*str(b[i]),*str(a[i]))
        c.append(int(l[i]))
        c.append(int(b[i]))
        continue