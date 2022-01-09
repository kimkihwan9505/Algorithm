a = int(input())
num=[]
for _ in range(a):
    [b,c] = map(int,input().split()) 
    num.append([c,b])    # (key=lambda x:x(x[1],x[0])) 이 오류나서 처음부터 역순으로 넣었다 
num.sort()
for i in range(a):
    print(num[i][1],num[i][0])    
    
