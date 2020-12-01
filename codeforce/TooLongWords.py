case = int(input())
ctr = 0
x = []
while ctr<case:
    word = input().strip()
    if len(word)>10:
        x.append(f'{word[0]}{len(word)-2}{word[-1]}')
    else:
        x.append(word)
    ctr += 1
for i in x:
    print(i)
