a,b = map(int,input().split())
lines=[]

for _ in range(a):
    lines.append(int(input()))    
    
start,end = 1 , max(lines)

while start <= end:
    mid=(start+end) //2  # 랜선길이 기준
    cnt=0
    for i in lines: 
        cnt += i //mid  
    if cnt >= b:
        start=mid + 1
    else :
        end = mid -1
print(end)
