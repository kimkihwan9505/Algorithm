a,b,c = map(int,input().split())

land = [list(map(int,input().split())) for i in range(a)]
top = max(max(land))
bottom = min(min(land))
times=[]
for i in range(top,bottom-1,-1):
    inv=c
    time =0
    for j in land: #land[j]
        for k in j: #land[j][k]
            need = i-k
            inv -=need
            if need > 0: #뺴기 1초
                time+=need
            elif need < 0:
                time+=need*-2 # 쌓기 2초
                
    if inv >= 0:
        times.append((time,i))
        
times=sorted(times,key = lambda time:time[0])
print(times[0][0],times[0][1])
