n = int(input())
count = 0
c = 1
for i in range(100):
    if i>1:
        for j in range(2,i):
            if(i%j)==0:
                break
        else:
            if count<15:
                count+=1
                if count<=n:
                    c*=i
print(c)
