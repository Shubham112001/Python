from datetime import time
h, m, s = input().split(":")
h1, m1, s1 = input().split(":")
oldTime = time(int(h), int(m), int(s))
newTime = time(int(h1), int(m1), int(s1))
diff = newTime-oldTime
print(diff)