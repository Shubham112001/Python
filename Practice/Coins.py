n = int(input())
d = int(input())
count = 1
while count<=7:
    if d == 7 or d == 1:
        n = n*2
        if d == 7:
            d = 1
        else:
            d += 1
    else:
        n += 5
        d += 1
    count += 1
print(n)
