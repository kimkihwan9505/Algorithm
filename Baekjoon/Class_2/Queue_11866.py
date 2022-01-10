a,b = map(int,input().split())
num=[]
for i in range(1,a+1):
    num.append(i)
    
print("<",end='')

while len(num):
    for i in range(b-1):
        num.append(num.pop(0)) #인덱스 전까지 뺴서 뒤에 다시 붙히고 0번쨰를 뺀다 
    print(num.pop(0),end='')
    if len(num) !=0:
        print(",",end=' ')
        
print(">")
