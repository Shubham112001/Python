n = int(input())
a = input().split(" ")
count = 0
lst = []
c = 0
for i in a:
    count += int(i)
print(count)
for i in range(count):
    for j in range(len(a)):
        lst.append(j)
        for k in range(1, int(j+1)):
            c += k
            lst.append(c)
    print(lst)
    if i not in lst:
        print(i)

