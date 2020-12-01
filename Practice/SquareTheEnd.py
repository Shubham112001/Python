def squareTheEnds(N):
    a=N[0]
    b=N[-1]
    Sum=''
    for i in range(1,len(N)-1):
        Sum+=str(N[i])
    X=str(int(a)**2)+Sum+str(int(b)**2)
    return X
N=input()
print(squareTheEnds(N))