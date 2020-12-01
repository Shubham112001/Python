n=int(input())
a=n*2
b=0
c=0
for i in range(n,0,-1):
    c+=1
    print('*'*(n-c)+str(c)+str(i-1))
