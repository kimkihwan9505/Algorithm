
import sys
input = sys.stdin.readline

a,b =list(map(int,input().split()))

dic={}
for i in range(1,a+1):
    name=input().rstrip()
    dic[i]=name # i 자리에 이름을 넣고 이름자리에 숫자 넣기 -> a:1 , b:2 ~~~
    dic[name]=i


for _ in range(b):
    find=input().rstrip()
    if find.isdigit():
        print(dic[int(find)])
    else :
        print(dic[find])      
        
