n, k = input().split(" ")
a = input().split(" ")
c = 0
for i in a:
    if int(i)>int(k):
        c+=1
print(c)