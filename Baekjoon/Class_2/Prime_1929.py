a,b = map(int,input().split())
for i in range(a, b+1 ):
    if i == 1:
        continue
    for j in range(2,int(i**0.5)+1): # 제곱근 까지만 구한다 
        if i % j==0:
            break
    else :
        print(i)
        
 '''
 
a,b = map(int,input().split())
num=[]
for i in range(a,b+1):
    count=0                
    for j in range(1,i+1):
        if i%j == 0:
            count+=1
            if count == 2:
                if i == j:
                    num.append(i)
  시간초과
  '''
