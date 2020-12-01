r, c =map(int, input().split())
mat = [list(input().split())for i in range(r)]
lst = []
for i in range(r):
    print(*mat[i])
    a = max(mat[i][0])
    lst.append(a)
print(lst)