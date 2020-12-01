he
    l1.append(a[i])
    if int(a[i])%2==0:
        l.append(a[i])
z=max(l)
for i in range(len(a)):
    if int(a[i])==int(z):
        lst1.append(a[i])
        continue
    lst.append(a[i])
lst.sort()
print(*lst,*lst1)
