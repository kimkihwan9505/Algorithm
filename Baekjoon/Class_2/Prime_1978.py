a=int(input())
num=list(map(int,input().split()))


def prime(num):
    if num ==1:
        return False
    elif num ==2:
        return True
    for i in range(2,num):
        if num % i ==0:
            return False
    return True
cnt=0

for i in num:
    if prime(i) is True:
        cnt+=1
print(cnt)
