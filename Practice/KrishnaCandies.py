n = list(map(int, input().split(" ")))
n.sort()
t = n[0] + n[1]
lst = []
for i in range(2, len(n)):
    t += n[i]
    lst.append(t)
a = n[0] + n[1]
lst.append(a)
print(sum(lst))