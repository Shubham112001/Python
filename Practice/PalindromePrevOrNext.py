import sys

print("Hello World")
s = input()
if len(s) % 2 == 0:
    n = len(s) // 2
else:
    n = (len(s) // 2) + 1
print(s, n)
j = -1
x = True
for i in range(n):
    a = ord(s[i])
    b = ord(s[j])
    if s[i] == 'a' or s[i] == 'A':
        if a == b or a + 1 == b or a + 2 == b:
            x = True
        else:
            sys.exit('False')
    elif s[i] == 'z' or s[i] == 'Z':
        if a == b or a - 1 == b or a + 2 == b:
            x = True
        else:
            sys.exit('False')
    elif s[i] == 'b' or s[i] == 'B':
        if a == b or a - 1 == b or a + 1 == b:
            x = True
        else:
            sys.exit('False')
    elif s[i] == 'y' or s[i] == 'Y':
        if a == b or a - 1 == b or a + 1 == b:
            x = True
        else:
            sys.exit('False')

    elif a == b or a - 1 == b or a + 1 == b or a + 2 == b or a - 2 == b:
        x = True
    else:
        sys.exit('False')
    print(a, b)
    j -= 1
print(x)