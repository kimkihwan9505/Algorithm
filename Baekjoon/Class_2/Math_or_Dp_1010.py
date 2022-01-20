#-------------Math
def factoriral(n):
    num=1
    for i in range(1,n+1):
        num*=i
    return num
t= int(input())
for _ in range(t):
    a,b= map(int,input().split())
    print(factoriral(b)//(factoriral(a)*factoriral(b-a)))

#---------------DP

