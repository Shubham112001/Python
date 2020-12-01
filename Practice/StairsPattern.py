S=input().strip()
L=(len(S)*2)-1
ctr=0
for i in range(1,L+1):
    if i <=len(S):
        print('-'*(len(S)-i),end='')
        print(S[0:i])
    if i >=len(S):
        print(S[ctr+1:])
        ctr+=1