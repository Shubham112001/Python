M, N = input().split(" ")
print(M,N)
c = 0
lst = []
if int(M) > 1:
    for i in range(2,int(M)):
        if (int(M) % i) == 0:
            #print(M,"is not a prime number")
            #for j in range(1, int(M)):
            while i<int(M):
                if int(M) % i == 0:
                    lst.append(i)
                    i+=1
                    if int(M) == int(N):
                        print(c)
                    continue
                a = max(lst)
                print(a)
                c+=1
                M = a


    else:
        c+=1
print(c)
