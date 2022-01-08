
a = int(input())
six_n =666
cnt=0

while 1: # 계속 더하면서 '666'이 포함될때만 cnt +1 
    if '666' in str(six_n):
        cnt+=1
    if cnt==a:
        print(six_n)
        break
    six_n+=1
        
