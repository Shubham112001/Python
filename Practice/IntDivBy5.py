m,n=map(int,input().split())
seei,seej=set(),set()
x,y,ctr=min(m,n),max(m,n),0
for i in range(1,y+1):
    for j in range(1,x+1):
       if (i+j)%5==0 and j not in seej and i not in seei:
           ctr+=1
           seej.add(j)
           seei.add(i)
print(ctr)