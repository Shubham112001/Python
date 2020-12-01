s=input()
a=s+'d'
lst=[]
rep=[]
count=0
for i in range(0,len(a),1):
    if i==len(s):
        break
    if a[i]!='s':
        continue
    if a[i]=='s' and a[i+1]=='r' and i+1 not in rep:
        count+=2
        rep.append(a[i+1])
    if a[i]=='s' and a[i+1]!='r'and i+1 not in rep:
        rep.append(i+1)
        count+=1
        lst.append(count)
        continue
v=max(lst)
print(lst,v)

