a = int(input())
b= list(map(int,input().split()))
c=0
d=0
b.sort()
for i in range(a):
    c+=b[i]
    d+=c
print(d)
