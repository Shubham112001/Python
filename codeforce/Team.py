n = int(input())
c = 0
for i in range(n):
    count = 0
    a = input().split(" ")
    for i in a:
        if int(i)==1:
            count+=1
    if count>=2:
        c+=1
print(c)