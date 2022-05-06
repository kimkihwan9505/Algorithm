a = int(input())
r=[]
for _ in range(a):
    start,end = map(int,input().split())
    r.append([start,end])    
r = sorted(r, key=lambda a: a[0])    
r = sorted(r, key=lambda a: a[1])

last = 0
cnt =0

for i,j in r:
    if i >= last:
        cnt+=1
        last=j
print(cnt)
