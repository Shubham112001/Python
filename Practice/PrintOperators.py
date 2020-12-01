N=int(input())
s=''
a=input().split(" ")
P,Q=input().split(" ")
for i in range(len(a)):
    if int(P)//int(Q)==int(a[i]):
        s+='/'
    elif int(P)*int(Q)==int(a[i]):
        s+='*'
    elif int(P)+int(Q)==int(a[i]):
        s+='+'
    elif int(P)-int(Q)==int(a[i]):
        s+='-'
    else:
        s+='#'
print(s)