while 1:
    a=list(input())
    if int(a[0])==0: 
        break
    if a==a[-1::-1]: # 역순배열시 원래 문자열과 같으면 팰린드롬수 
        print('yes')
    else:
        print("no") 
