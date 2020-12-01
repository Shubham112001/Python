n = int(input())
a = list(input().split())
lst = []
count = 0
q = 0
for i in range(len(a)):
    if count < 5:
        if i < 0 and q < 3:
            lst.append(a[i])
            #print(a[i], end= " ")
            count += 1
            q += 1
        elif i > 0:
            lst.append(a[i])
            #print(a[i], end= " ")
            count += 1
        count = 0
print(lst, end=", ")
