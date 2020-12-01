x, y = map(int,input().split(" "))
xint = input().split(" ")
yint = input().split(" ")
z = []
#print(int(xint[0]))
for i in xint:
    for j in yint:
        a = int(i)
        if int(i) == int(j) and a not in z:
            z.append(a)
print(*z)