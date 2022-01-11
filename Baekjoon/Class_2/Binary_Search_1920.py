a=int(input())
b=list(map(int,input().split()))
b.sort()
c=int(input())
d=list(map(int,input().split()))


for i in d:
    left,right=0,a-1
    while left < right:
        mid=(left+right)//2
        if b[mid] < i :
            left=mid+1
        else :
            right=mid
    if i ==b[right]:
        print(1)
    else :
        print(0)
'''
처음 미드값으로 비교한다음 -> 크다면 left값이 mid+1 작다면 mid 값이 right가 되어야한다
'''
