n = int(input())
x = input().split(" ")
a = []
for i in x:
    for j in range(2,11):
        if int(i[:2]) % j == 0 and int(i[-2:]) % j  == 0:
            a.append(i)
if a not in []:
    print(a)
else:
    print("-1")
