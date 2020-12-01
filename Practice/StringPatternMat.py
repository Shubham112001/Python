import numpy as np
s1=input()
s2=input().split(' ')
a=0
f=False
lst=[]
while a<len(s1):
    b=np.array(s1[a])
    c=np.array(s2[a])
    d=np.equal(b,c)
    lst.append(d)
    a+=1
if False in lst:
    print('No')
else:
    print('Yes')

