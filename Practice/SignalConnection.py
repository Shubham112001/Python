N = int(input())
if N<100000 and N>=1:
    latitude = input().split(" ")
    longitude = input().split(" ")
    h = input().split(" ")
    l, lo = input().split(" ")
    count = 0
    for i in range(N):
        a = float(latitude[i])
        b = float(longitude[i])
        c = float(h[i])
        if float(l) > a - c and float(l) < a + c and float(lo) > b - c and float(lo) < b + c:
            count += 1
    print(count)
