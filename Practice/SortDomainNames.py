lst = []
n = int(input())
for i in range(n):
    string,a = input().strip().split('@')
    lst.append(a)
lst.sort()
lst = sorted(lst, key=lst.count, reverse= True)
mail=[]
for i in lst:
    if i not in mail:
        mail.append(i)
print(*mail,sep="\n")

