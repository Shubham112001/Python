n = int(input("No of integers: "))
a = list(map(int,input().split(" ")))
m = a[:]
print(a)
b = len(a)
flag = 0

for i in range(b):
    if a[i]%2 == 0 and flag == 0:
        j = i
        flag = 1
        continue
    elif a[i]%2 == 0 and flag == 1:
        m[j] = a[i]
        m[i] = a[j]
        flag = 0

print(m)
