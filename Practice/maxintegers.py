lst = []
a= int(input("Enter no of integers"))
for i in range(a):
    b = list(map(int,input()))
    lst += b
    lst.sort()
m = len(lst)
e = max(lst)
d = min(lst)
k = []
f = []
g = {}
q = list(range(d, e))
for i in q:
    if i not in lst:
        k.append(i)
for i in lst:
    if i not in g:
        g[i] = 1
    else:
        if g[i] == 1:
            f.append(i)
        g[i] += 1

print(f)
print(k)
