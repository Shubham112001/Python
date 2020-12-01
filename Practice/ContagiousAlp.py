a = input()
i = 0
while True:
    if a[i] in a:
        j = i + 1
        
        if ord(a[i+1]) == ord(a[j]):
            x = a[i]+a[j]
            print(x)
    i += 1
