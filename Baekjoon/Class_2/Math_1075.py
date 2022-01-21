a=input()
b=int(input())
num=int(a[:-2]+'00')

while 1:
    if num % b ==0:
        break
    else:
        num+=1
print(str(num)[-2:])
