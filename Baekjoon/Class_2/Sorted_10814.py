a = int(input())
b=[]
for _ in range(a):
    c=input().split()
    b.append(c)    
    
b.sort(key=lambda x: int(x[0])) # index[0]번째인 나이순으로 정렬

for i in range(a):
    print(b[i][0],b[i][1])
