a = int(input())
lst = []
q = []
while a>0:
    b = a % 2
    a = a//2
    lst.append(b)
lst.reverse()
#for i in range(len(lst)):
i = 0
while i < len(lst):
    z = list(lst)
    if lst[i] == 1:
        z[i] = 0
    else:
        z[i] = 1
    #print(z)
    count = 0
    c = len(lst)-1
    for j in z:
        count += int(j)*(2**c)
        q.append(count)
        c -= 1
    i += 1
print(max(q))
