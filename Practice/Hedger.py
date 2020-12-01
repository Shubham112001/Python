N,k,a=map(int,input().split())
pstock=list(map(float,input().split()))
capamount=list(map(float,input().split()))
combi=[]
for i in range(N):
    combi.append([capamount[i],pstock[i]])
combi.sort()
sol=combi[N-k:]
sol.sort(key=lambda x:x[1])
nstock=[]
ctr,x=0,0
dup=[0]*len(sol)
amount=a
while True:
    for i in range(len(sol)):
        if amount >= sol[i][1]:
            amount-=sol[i][1]
            dup[i]+=1
            ctr+=1
    if x!=ctr:
        x=ctr
    else:
        break
profit=[]
for i in range(len(sol)):
    profit.append(dup[i]*sol[i][0]*sol[i][1]/100)
print(round(sum(profit)))
