a=int(input())
fac=1
for i in range(1,a+1):
    fac*=i
count=0
for i in str(fac)[::-1]:
    if i != '0':
        break
    else :
        count+=1
print(count)
'''
import Math 안의 factorial함수 사용가능
'''
