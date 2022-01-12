while 1:
    a=input()
    tmp=[]
    if a =='.':
        break            
    for i in a:
        if i=='(' or i=='[':
            tmp.append(i)
        elif i==']':
            if len(tmp) != 0 and tmp[-1]=='[':
                tmp.pop()
            else :
                tmp.append(']')
                break
        elif i ==')':
            if len(tmp) != 0 and tmp[-1] =='(':
                tmp.pop()
            else :
                tmp.append(')')
                break
    if len(tmp) ==0:
        print('yes')
    else :
        print('no')
    
