a=int(input())
result=0
for i in range(1,a+1):
    num=list(map(int,str(i))) #생성자 찾기
    result=i+sum(num)
    if result==a:
        print(i)
        break
    if i==a: #생성자없으면 
        print(0)
