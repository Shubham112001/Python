a = input().split(" ")
lst = []
count = 0
c = 0
#print(a)
for i in a:
    #print(i)
    lst.append(i)
#print(lst)
for i in range(0,len(lst),2):
    #print(lst[i])
    count += int(lst[i])
for i in range(1,len(lst),2):
    #print(lst[i])
    c += int(lst[i])
b = max(c,count)
print(b)