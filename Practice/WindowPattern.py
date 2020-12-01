n,x=map(int,input().split())
s=int(x**0.5)
print('+'+('-'*n+'+')*s)
for i in range(s):
    for j in range(n):
        print('|'+('*'*n+'|')*s)
    print('+'+('-'*n+'+')*s)