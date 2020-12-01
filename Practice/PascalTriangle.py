n = int(input())
x = []
for i in range(1, n+1):
    s=''
    c = 1
    for j in range(1, i+1):
        s = s+str(c)+' '
        c = int(c*(i-j)/j)
    x.append(s)
print(s)