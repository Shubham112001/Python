N = input("The no of brides and groom taking part:")
a = input()
b = input()
m = len(a)
count = 0
for i in a:
    for j in b:
        if i == j:
            count += 1
            a = a.replace(i, '', 1)
            b = b.replace(j, '', 1)
        else:
            break
d = m-count
print(d)
