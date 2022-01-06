a,b =list(map(int,input().split()))
c =list(map(int,input().split()))
sum=[]
for i in range(len(c)): # 처음부터 
    for j in range(i+1,len(c)): # 그다음인덱스부터 
        for h in range(j+1,len(c)): # 그다음 인덱스부터 0,1,2 ->0,1,3-> 다돌면 1,2,3->1,2,4 ~~
            sum.append(c[i]+c[j]+c[h]) #모든 수의 합을 리스트에 담고
            
search=[]
for i in sum:
    if i <=b:
        search.append(i) # 리스트에 담긴 수들을 처음 선언한 b 와 비교해서 같거나 작은것중 최댓값 찾기

print(max(search))        
