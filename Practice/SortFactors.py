n = int(input())
lst = []
lst1 = []
for i in range(1, n+1):
    if n%i == 0:
        lst.append(i)
print(lst)
for i in range(1, len(lst)+1):
    count = 0
    print(lst[i])
    for j in range(1, i+1):
        if i%j == 0:
            count += 1
    lst1.append(count)
#lst1.sort()
print(lst1)
