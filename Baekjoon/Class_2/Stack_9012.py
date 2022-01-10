a = int(input())
for _ in range(a):
    ps = list(map(str, input()))
    sum=0
    for i in ps:
        if i =='(':
            sum+=1
        elif i ==')' :
            sum-=1
            if sum==-1:
                print('NO')
                break
    if sum >0:
        print('NO')
    elif sum == 0:
        print('YES')
 #-----------------------Stack-------------------#
a=int(input())
for _ in range(a):        
    data=input()
    stack=[]
    for i in data :
        if i == '(':
            stack.append(i)
        elif i ==')':
            if len(stack) != 0:
                stack.pop(0)
            else :
                stack.append(i)
                break
    if len(stack) == 0:
        print('YES')
    elif len(stack) != 0:
        print('NO')
        
            
