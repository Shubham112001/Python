s1=input()
s2=input()
x=int(input())
lst=[]
a=0
while a<=x:
    for i in range(len(s1)):
        if s1[i] in s2 and i not in lst:
            lst.append(i)
            print('yes')
    a+=1


