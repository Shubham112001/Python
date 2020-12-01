n = input()
b = len(n)
lst = []
for i in range(b):
    if int(n[i]) != 0:
        if int(n[i])%2 == 0:
            lst += n[i]
            a = n[i]
            for j in range(i+1, b):
                a += n[j]
                if int(a) %2 == 0:
                    lst += [a]
print(len(lst))



