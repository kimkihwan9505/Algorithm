N=int(input())
arr=[]
for i in range(N):
    a,b = map(int,input().split()) # c=input().split() 로 할 경우 오류 방생 
    arr.append((a,b))
arr.sort()
for i in range(N):
    print(arr[i][0],arr[i][1])
   
