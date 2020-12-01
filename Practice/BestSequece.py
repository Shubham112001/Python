p = input()
ch = list(input().split())
l, k = [], []
ind, samp, fch = [], [], []
ctr = 0
for i in p:
    if ch[ctr] == i:
        if i not in samp:
            ind.append([p.index(i), i])
            samp.append(i)
            ctr += 1
        if ctr == len(ch):
            break
ind.sort()
for i in ind:
    fch.append(i[1])
for i in fch:
    l.append([i, p.count(i)])
for i in l:
    k += i[0]
print(*k, sep='')