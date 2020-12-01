N = input()
count = 0
z = []
for i in range(len(N)-1):
    for j in range(i+1,len(N)-1):
        x = (N[i], N[j])
        y = ([j], N[i])
        if int(N[i]) + int(N[j]) == int(N[-1]) and x not in z and y not in z:
            z += [x]
            z += [y]
            count += 1
if count != 0:
    print(count)
else:
    print(-1)

