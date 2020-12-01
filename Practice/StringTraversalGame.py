s1 = input()
s2 = input()
ctr,s=len(s1),''
vowels=['a','e','i','o','u','A','E','I','O','U']
while ctr>=0:
    if s1[ctr] in vowels and s2[ctr] in vowels or s1[ctr] not in vowels and s2[ctr] not in vowels:
        s+=s1[ctr]+s2[ctr]
        s1,s2=s2,s1
    else:
        s+=s1[ctr]
    ctr-=1
print(s)